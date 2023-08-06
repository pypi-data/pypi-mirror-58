"""Tests for the fix_ffvt3rskinpartition spell"""
from tests.scripts.nif import call_niftoaster
from tests.utils import BaseNifFileTestCase


class TestFixSkinPartitionNif(BaseNifFileTestCase):
    """Invoke the fix_ffvt3rskinpartition spell check through nif toaster"""

    def setUp(self):
        super(TestFixSkinPartitionNif, self).setUp()
        self.src_name = "test_fix_ffvt3rskinpartition.nif"
        super(TestFixSkinPartitionNif, self).copyFile()
        super(TestFixSkinPartitionNif, self).readNifData()

    def test_non_interactive_fix_vertex_skin_partition(self):
        """Test that we can repartition vertex weight influence"""

        call_niftoaster("--raise", "fix_ffvt3rskinpartition", "--noninteractive", "--verbose=1", self.dest_file)

        """
        pyffi.toaster:INFO:=== tests/spells/nif/files/test_fix_ffvt3rskinpartition.nif ===
        pyffi.toaster:INFO:  --- fix_ffvt3rskinpartition ---
        pyffi.toaster:INFO:    ~~~ NiNode [Bip01] ~~~
        pyffi.toaster:INFO:      ~~~ NiNode [Bip01 Pelvis] ~~~
        pyffi.toaster:INFO:        ~~~ NiNode [Bip01 Spine] ~~~
        pyffi.toaster:INFO:          ~~~ NiNode [Bip01 Spine1] ~~~
        pyffi.toaster:INFO:            ~~~ NiNode [Bip01 Spine2] ~~~
        pyffi.toaster:INFO:              ~~~ NiNode [Bip01 Neck] ~~~
        pyffi.toaster:INFO:                ~~~ NiNode [Bip01 Head] ~~~
        pyffi.toaster:INFO:                ~~~ NiNode [Bip01 L Clavicle] ~~~
        pyffi.toaster:INFO:                  ~~~ NiNode [Bip01 L UpperArm] ~~~
        pyffi.toaster:INFO:                    ~~~ NiNode [Bip01 L Forearm] ~~~
        pyffi.toaster:INFO:                ~~~ NiNode [Bip01 R Clavicle] ~~~
        pyffi.toaster:INFO:                  ~~~ NiNode [Bip01 R UpperArm] ~~~
        pyffi.toaster:INFO:                    ~~~ NiNode [Bip01 R Forearm] ~~~
        pyffi.toaster:INFO:          ~~~ NiNode [Bip01 L Thigh] ~~~
        pyffi.toaster:INFO:            ~~~ NiNode [Bip01 L Calf] ~~~
        pyffi.toaster:INFO:              ~~~ NiNode [Bip01 L Foot] ~~~
        pyffi.toaster:INFO:                ~~~ NiNode [Bip01 L Toe0] ~~~
        pyffi.toaster:INFO:          ~~~ NiNode [Bip01 R Thigh] ~~~
        pyffi.toaster:INFO:            ~~~ NiNode [Bip01 R Calf] ~~~
        pyffi.toaster:INFO:              ~~~ NiNode [Bip01 R Foot] ~~~
        pyffi.toaster:INFO:                ~~~ NiNode [Bip01 R Toe0] ~~~
        pyffi.toaster:INFO:      ~~~ NiTriShape [Body] ~~~
        pyffi.toaster:INFO:        updating skin partition
        pyffi.nif.nitribasedgeom:INFO:Counted minimum of 1 and maximum of 3 bones per vertex
        pyffi.nif.nitribasedgeom:INFO:Imposing maximum of 4 bones per vertex.
        pyffi.nif.nitribasedgeom:INFO:Imposing maximum of 4 bones per triangle (and hence, per partition).
        pyffi.nif.nitribasedgeom:INFO:Creating partitions
        pyffi.nif.nitribasedgeom:INFO:Created 12 small partitions.
        pyffi.nif.nitribasedgeom:INFO:Merging partitions.
        pyffi.nif.nitribasedgeom:INFO:Skin has 12 partitions.
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 0
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 1
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 2
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 3
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 4
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 5
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 6
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 7
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 8
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 9
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 10
        pyffi.nif.nitribasedgeom:INFO:Optimizing triangle ordering in partition 11
        pyffi.toaster:INFO:  writing to temporary file
        pyffi.toaster:INFO:Finished.
        """
