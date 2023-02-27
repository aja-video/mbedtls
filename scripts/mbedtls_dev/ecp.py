"""Framework classes for generation of ecp test cases."""
# Copyright The Mbed TLS Contributors
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List

from . import test_data_generation
from . import bignum_common

class EcpTarget(test_data_generation.BaseTarget):
    #pylint: disable=abstract-method, too-few-public-methods
    """Target for ecp test case generation."""
    target_basename = 'test_suite_ecp.generated'

class EcpP192R1Raw(bignum_common.ModOperationCommon,
                   EcpTarget):
    """Test cases for ecp quasi_reduction()."""
    symbol = "-"
    test_function = "ecp_mod_p192_raw"
    test_name = "ecp_mod_p192_raw"
    input_style = "fixed"
    arity = 1

    moduli = ["fffffffffffffffffffffffffffffffeffffffffffffffff"] # type: List[str]

    input_values = [
        "0", "1",

        # Modulus - 1
        "fffffffffffffffffffffffffffffffefffffffffffffffe",

        # First 8 number generated by random.getrandbits(384) - seed(2,2)
        ("cf1822ffbc6887782b491044d5e341245c6e433715ba2bdd"
         "177219d30e7a269fd95bafc8f2a4d27bdcf4bb99f4bea973"),
        ("ffed9235288bc781ae66267594c9c9500925e4749b575bd1"
         "3653f8dd9b1f282e4067c3584ee207f8da94e3e8ab73738f"),
        ("ef8acd128b4f2fc15f3f57ebf30b94fa82523e86feac7eb7"
         "dc38f519b91751dacdbd47d364be8049a372db8f6e405d93"),
        ("e8624fab5186ee32ee8d7ee9770348a05d300cb90706a045"
         "defc044a09325626e6b58de744ab6cce80877b6f71e1f6d2"),
        ("2d3d854e061b90303b08c6e33c7295782d6c797f8f7d9b78"
         "2a1be9cd8697bbd0e2520e33e44c50556c71c4a66148a86f"),
        ("fec3f6b32e8d4b8a8f54f8ceacaab39e83844b40ffa9b9f1"
         "5c14bc4a829e07b0829a48d422fe99a22c70501e533c9135"),
        ("97eeab64ca2ce6bc5d3fd983c34c769fe89204e2e8168561"
         "867e5e15bc01bfce6a27e0dfcbf8754472154e76e4c11ab2"),
        ("bd143fa9b714210c665d7435c1066932f4767f26294365b2"
         "721dea3bf63f23d0dbe53fcafb2147df5ca495fa5a91c89b"),

        # Next 2 number generated by random.getrandbits(192)
        "47733e847d718d733ff98ff387c56473a7a83ee0761ebfd2",
        "cbd4d3e2d4dec9ef83f0be4e80371eb97f81375eecc1cb63"
    ]

    @property
    def arg_a(self) -> str:
        return super().format_arg('{:x}'.format(self.int_a)).zfill(2 * self.hex_digits)

    def result(self) -> List[str]:
        result = self.int_a % self.int_n
        return [self.format_result(result)]

    @property
    def is_valid(self) -> bool:
        return True

class EcpP224R1Raw(bignum_common.ModOperationCommon,
                   EcpTarget):
    """Test cases for ecp quasi_reduction()."""
    symbol = "-"
    test_function = "ecp_mod_p224_raw"
    test_name = "ecp_mod_p224_raw"
    input_style = "arch_split"
    arity = 1

    moduli = ["ffffffffffffffffffffffffffffffff000000000000000000000001"] # type: List[str]

    input_values = [
        "0", "1",

        # Modulus - 1
        "ffffffffffffffffffffffffffffffff000000000000000000000000",

        # Maximum canonical P224 multiplication result
        ("ffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
         "ffffffffffffffffffffffffffffffffffffffffffffffffffffffff"),

        # Generate an overflow during reduction
        ("00000000000000000000000000010000000070000000002000001000"
         "FFFFFFFFFFFF9FFFFFFFFFE00000EFFF000070000000002000001003"),

        # Generate an underflow during reduction
        ("00000001000000000000000000000000000000000000000000000000"
         "00000000000DC0000000000000000001000000010000000100000003"),

        # First 8 number generated by random.getrandbits(448) - seed(2,2)
        ("da94e3e8ab73738fcf1822ffbc6887782b491044d5e341245c6e4337"
         "15ba2bdd177219d30e7a269fd95bafc8f2a4d27bdcf4bb99f4bea973"),
        ("cdbd47d364be8049a372db8f6e405d93ffed9235288bc781ae662675"
         "94c9c9500925e4749b575bd13653f8dd9b1f282e4067c3584ee207f8"),
        ("defc044a09325626e6b58de744ab6cce80877b6f71e1f6d2ef8acd12"
         "8b4f2fc15f3f57ebf30b94fa82523e86feac7eb7dc38f519b91751da"),
        ("2d6c797f8f7d9b782a1be9cd8697bbd0e2520e33e44c50556c71c4a6"
         "6148a86fe8624fab5186ee32ee8d7ee9770348a05d300cb90706a045"),
        ("8f54f8ceacaab39e83844b40ffa9b9f15c14bc4a829e07b0829a48d4"
         "22fe99a22c70501e533c91352d3d854e061b90303b08c6e33c729578"),
        ("97eeab64ca2ce6bc5d3fd983c34c769fe89204e2e8168561867e5e15"
         "bc01bfce6a27e0dfcbf8754472154e76e4c11ab2fec3f6b32e8d4b8a"),
        ("a7a83ee0761ebfd2bd143fa9b714210c665d7435c1066932f4767f26"
         "294365b2721dea3bf63f23d0dbe53fcafb2147df5ca495fa5a91c89b"),
        ("74667bffe202849da9643a295a9ac6decbd4d3e2d4dec9ef83f0be4e"
         "80371eb97f81375eecc1cb6347733e847d718d733ff98ff387c56473"),

        # Next 2 number generated by random.getrandbits(224)
        "eb9ac688b9d39cca91551e8259cc60b17604e4b4e73695c3e652c71a",
        "f0caeef038c89b38a8acb5137c9260dc74e088a9b9492f258ebdbfe3"
    ]

    @property
    def arg_a(self) -> str:
        hex_digits = bignum_common.hex_digits_for_limb(448 // self.bits_in_limb, self.bits_in_limb)
        return super().format_arg('{:x}'.format(self.int_a)).zfill(hex_digits)

    def result(self) -> List[str]:
        result = self.int_a % self.int_n
        return [self.format_result(result)]

    @property
    def is_valid(self) -> bool:
        return True
class EcpP521R1Raw(bignum_common.ModOperationCommon,
                   EcpTarget):
    """Test cases for ecp quasi_reduction()."""
    test_function = "ecp_mod_p521_raw"
    test_name = "ecp_mod_p521_raw"
    input_style = "arch_split"
    arity = 1

    moduli = [("01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
               "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
             ] # type: List[str]

    input_values = [
        "0", "1",

        # Corner case: maximum canonical P521 multiplication result
        ("0003ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
         "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
         "fffff800"
         "0000000000000000000000000000000000000000000000000000000000000000"
         "0000000000000000000000000000000000000000000000000000000000000004"),

        # Test case for overflow during addition
        ("0001efffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
         "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
         "000001ef"
         "0000000000000000000000000000000000000000000000000000000000000000"
         "000000000000000000000000000000000000000000000000000000000f000000"),

        # First 8 number generated by random.getrandbits(1042) - seed(2,2)
        ("0003cc2e82523e86feac7eb7dc38f519b91751dacdbd47d364be8049a372db8f"
         "6e405d93ffed9235288bc781ae66267594c9c9500925e4749b575bd13653f8dd"
         "9b1f282e"
         "4067c3584ee207f8da94e3e8ab73738fcf1822ffbc6887782b491044d5e34124"
         "5c6e433715ba2bdd177219d30e7a269fd95bafc8f2a4d27bdcf4bb99f4bea973"),
        ("00017052829e07b0829a48d422fe99a22c70501e533c91352d3d854e061b9030"
         "3b08c6e33c7295782d6c797f8f7d9b782a1be9cd8697bbd0e2520e33e44c5055"
         "6c71c4a6"
         "6148a86fe8624fab5186ee32ee8d7ee9770348a05d300cb90706a045defc044a"
         "09325626e6b58de744ab6cce80877b6f71e1f6d2ef8acd128b4f2fc15f3f57eb"),
        ("00021f15a7a83ee0761ebfd2bd143fa9b714210c665d7435c1066932f4767f26"
         "294365b2721dea3bf63f23d0dbe53fcafb2147df5ca495fa5a91c89b97eeab64"
         "ca2ce6bc"
         "5d3fd983c34c769fe89204e2e8168561867e5e15bc01bfce6a27e0dfcbf87544"
         "72154e76e4c11ab2fec3f6b32e8d4b8a8f54f8ceacaab39e83844b40ffa9b9f1"),
        ("000381bc2a838af8d5c44a4eb3172062d08f1bb2531d6460f0caeef038c89b38"
         "a8acb5137c9260dc74e088a9b9492f258ebdbfe3eb9ac688b9d39cca91551e82"
         "59cc60b1"
         "7604e4b4e73695c3e652c71a74667bffe202849da9643a295a9ac6decbd4d3e2"
         "d4dec9ef83f0be4e80371eb97f81375eecc1cb6347733e847d718d733ff98ff3"),
        ("00034816c8c69069134bccd3e1cf4f589f8e4ce0af29d115ef24bd625dd961e6"
         "830b54fa7d28f93435339774bb1e386c4fd5079e681b8f5896838b769da59b74"
         "a6c3181c"
         "81e220df848b1df78feb994a81167346d4c0dca8b4c9e755cc9c3adcf515a823"
         "4da4daeb4f3f87777ad1f45ae9500ec9c5e2486c44a4a8f69dc8db48e86ec9c6"),
        ("000397846c4454b90f756132e16dce72f18e859835e1f291d322a7353ead4efe"
         "440e2b4fda9c025a22f1a83185b98f5fc11e60de1b343f52ea748db9e020307a"
         "aeb6db2c"
         "3a038a709779ac1f45e9dd320c855fdfa7251af0930cdbd30f0ad2a81b2d19a2"
         "beaa14a7ff3fe32a30ffc4eed0a7bd04e85bfcdd0227eeb7b9d7d01f5769da05"),
        ("00002c3296e6bc4d62b47204007ee4fab105d83e85e951862f0981aebc1b00d9"
         "2838e766ef9b6bf2d037fe2e20b6a8464174e75a5f834da70569c018eb2b5693"
         "babb7fbb"
         "0a76c196067cfdcb11457d9cf45e2fa01d7f4275153924800600571fac3a5b26"
         "3fdf57cd2c0064975c3747465cc36c270e8a35b10828d569c268a20eb78ac332"),
        ("00009d23b4917fc09f20dbb0dcc93f0e66dfe717c17313394391b6e2e6eacb0f"
         "0bb7be72bd6d25009aeb7fa0c4169b148d2f527e72daf0a54ef25c0707e33868"
         "7d1f7157"
         "5653a45c49390aa51cf5192bbf67da14be11d56ba0b4a2969d8055a9f03f2d71"
         "581d8e830112ff0f0948eccaf8877acf26c377c13f719726fd70bddacb4deeec"),

        # Next 2 number generated by random.getrandbits(521)
        ("12b84ae65e920a63ac1f2b64df6dff07870c9d531ae72a47403063238da1a1fe"
         "3f9d6a179fa50f96cd4aff9261aa92c0e6f17ec940639bc2ccdf572df00790813e3"),
        ("166049dd332a73fa0b26b75196cf87eb8a09b27ec714307c68c425424a1574f1"
         "eedf5b0f16cdfdb839424d201e653f53d6883ca1c107ca6e706649889c0c7f38608")
    ]

    @property
    def arg_a(self) -> str:
        # Number of limbs: 2 * N
        return super().format_arg('{:x}'.format(self.int_a)).zfill(2 * self.hex_digits)

    def result(self) -> List[str]:
        result = self.int_a % self.int_n
        return [self.format_result(result)]

    @property
    def is_valid(self) -> bool:
        return True
