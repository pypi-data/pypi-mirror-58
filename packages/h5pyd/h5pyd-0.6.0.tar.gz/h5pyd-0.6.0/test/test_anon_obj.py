##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including          #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################
import logging
import config
if config.get("use_h5py"):
    import h5py
else:
    import h5pyd as h5py

from common import ut, TestCase


class TestAnonObj(TestCase):

    def test_create(self):
        filename = self.getFileName("anon_obj_test")
        print(filename)

        f = h5py.File(filename, 'w')
        self.assertTrue(f.id.id is not None)
        if not isinstance(f.id.id, str) or not f.id.id.startswith("g-"):
            # anon datasets only work with HSDS
            f.close()
            return
        self.assertTrue('/' in f)
        r = f['/']

        # create anonymous dataset
        dset = f.create_dataset(None, (10,), dtype="i4")

        dset_id = dset.id.id

        # write some values to the dataset
        dset[:] = list(range(10))

        # get a ref to the datset using the datset id
        dset_clone = f["datasets/" + dset_id]

        vals = dset_clone[:]
        self.assertEqual(list(vals), list(range(10)))

        self.assertEqual(len(f), 0)

        f.close()

        f = h5py.File(filename, 'r')
        self.assertTrue(f.id.id is not None)
        self.assertEqual(len(f), 0)

        dset = f["datasets/" + dset_id]

        vals = dset[:]
        self.assertEqual(list(vals), list(range(10)))

        f.close()

if __name__ == '__main__':
    loglevel = logging.ERROR
    logging.basicConfig(format='%(asctime)s %(message)s', level=loglevel)
    ut.main()
