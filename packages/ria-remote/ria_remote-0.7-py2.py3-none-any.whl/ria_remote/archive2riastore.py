# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""export a dataset from a RIA store to another RIA store"""

__docformat__ = 'restructuredtext'


import logging
import re
import posixpath
from datalad import cfg as dlcfg
from datalad.interface.base import (
    build_doc,
)
from datalad.interface.utils import eval_results
from datalad.support.param import Parameter
from datalad.support.constraints import (
    EnsureNone,
    EnsureStr,
)
from datalad.distribution.dataset import (
    Dataset,
    datasetmethod,
    EnsureDataset,
    require_dataset,
)
from datalad.distribution.clone import Clone
from .remote import RIARemote
from datalad.support.exceptions import InsufficientArgumentsError

lgr = logging.getLogger('ria_remote.install')


@build_doc
class Archive2Store(object):
    """
    """
    _params_ = dict(
        dataset=Parameter(
            args=("-d", "--dataset"),
            doc="""specify the dataset to export.  If
            no dataset is given, an attempt is made to identify the dataset
            based on the input and/or the current working directory""",
            constraints=EnsureDataset() | EnsureNone()),
        path=Parameter(
            args=("path",),
            metavar='PATH',
            doc="""path to a location for a temporary repository needed for the transfer""",
            constraints=EnsureStr() | EnsureNone()),
        store=Parameter(
            args=("-s", "--store"),
            doc="""name of the store to export data to""",
            # Note, that this ATM requires the dataset to already have both stores properly configured as remotes
            # (this also leads to -s as in "sibling" -> some thought should go into what would be a datalad-consistent
            # way to name that option)
            constraints=EnsureStr()),
    )

    @staticmethod
    @datasetmethod(name='ria_archive2store')
    @eval_results
    def __call__(
            path=None,
            dataset=None,
            store=None,
            # id=None    # Alternative to --dataset?
            # committish ? State to be exported?
    ):

        ds = require_dataset(dataset, check_installed=True, purpose='export to RIA store')

        if not path:
            raise InsufficientArgumentsError("a path is required")
        path = Path(path)

        if not store:
            raise InsufficientArgumentsError("a store to export to is required")

        throwaway = ria_install(source="inm7-storage:{ds_id}".format(ds_id=ds.id),
                                path=path,
                                ephemeral=True,
                                reckless=False,
                                return_type='item-or-list',
                                result_xfm='datasets'
                                )


########################################################################################

# TODO: commands move(well, copy) and fetch
#       keep transfering keys that way, but history and thereby merges via user's local ds
#
#
#
#


import sys
import os.path as op
from os import unlink
from pathlib import Path, PosixPath

from datalad.api import (
    Dataset,
    ria_install,
)
from datalad import ssh_manager
from ria_remote import RIARemote

dsid = sys.argv[1]
path = sys.argv[2]
jsc_base_path = Path(sys.argv[3])


ds = ria_install(source="inm7-storage:{ds_id}".format(ds_id=dsid),
                 path=path,
                 ephemeral=True,
                 reckless=False,
                 return_type='item-or-list',
                 result_xfm='datasets'
                 )
# TODO: we could actually use reckless, I think, if there was a way to only export what we need rather than the entire
#       annex/objects
#       -> double-check/fix export-archive

ds.run_procedure("cfg_inm7")
jsc_ds_location, jsc_archive_dir, _ = RIARemote.get_layout_locations(base_path=jsc_base_path, dsid=dsid)
# TODO: Store eventually needs to come from config/args (compute projects!)
#       Also: Since we are accessing via SSH anyway, and the remote end needs git, we could just read the remote config
#       for the store. Still needs some identification wrt the compute project, of course.
ds.siblings('add',
            name='jsc-store',
            url="ssh://jureca.fz-juelich.de:{ds_loc}".format(ds_loc=jsc_ds_location),
            fetch=True)
ds.get('.')
ds.ria_export_archive('.')
ssh = ssh_manager.get_connection("ssh://jureca.fz-juelich.de", use_remote_annex_bundle=False)
ssh.open()
# Note: the following should prob. be ensured by setting up the store (i.e.
# cfg_inm7?)
ssh("mkdir -p {archives}".format(archives=jsc_archive_dir))
ssh.put(source=op.join(ds.path, 'archive.7z'),  # needs absolute path, since CWD for SSH is not the ds root
        destination=str(PosixPath(jsc_ds_location / "archives")),
        recursive=False,
        preserve_attrs=False)
ssh.close()
unlink(op.join(ds.path, 'archive.7z'))
ds.repo.call_git(['branch', 'stage-commit'])
ds.repo.call_git(['push', 'jsc-store', 'HEAD', 'stage-commit'])

# TODO: We could now delete this throwaway clone
