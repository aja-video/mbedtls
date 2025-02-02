/*
 *  API(s) under test: psa_hash_compute()
 *
 *  Taken from programs/psa/psa_hash.c, and calls to all hash APIs
 *  but psa_hash_compute() removed.
 *
 *  Example computing a SHA-256 hash using the PSA Crypto API
 *
 *  The example computes the SHA-256 hash of a test string using the
 *  one-shot API call psa_hash_compute().
 *
 *
 *  Copyright The Mbed TLS Contributors
 *  SPDX-License-Identifier: Apache-2.0 OR GPL-2.0-or-later
 */

#include "psa/crypto.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "mbedtls/build_info.h"
#include "mbedtls/platform.h"

/* Information about hashing with the PSA API can be
 * found here:
 * https://arm-software.github.io/psa-api/crypto/1.1/api/ops/hashes.html
 *
 * The algorithm used by this demo is SHA 256.
 * Please see include/psa/crypto_values.h to see the other
 * algorithms that are supported by Mbed TLS.
 * If you switch to a different algorithm you will need to update
 * the hash data in the EXAMPLE_HASH_VALUE macro below. */

#if !defined(MBEDTLS_PSA_CRYPTO_C) || !defined(PSA_WANT_ALG_SHA_256)
int main(void)
{
    mbedtls_printf("MBEDTLS_PSA_CRYPTO_C and PSA_WANT_ALG_SHA_256"
                   "not defined.\r\n");
    return EXIT_SUCCESS;
}
#else

#define HASH_ALG PSA_ALG_SHA_256

const uint8_t sample_message[] = "Hello World!";
/* sample_message is terminated with a null byte which is not part of
 * the message itself so we make sure to subtract it in order to get
 * the message length. */
const size_t sample_message_length = sizeof(sample_message) - 1;

#define EXPECTED_HASH_VALUE {                                                    \
        0x7f, 0x83, 0xb1, 0x65, 0x7f, 0xf1, 0xfc, 0x53, 0xb9, 0x2d, 0xc1, 0x81, \
        0x48, 0xa1, 0xd6, 0x5d, 0xfc, 0x2d, 0x4b, 0x1f, 0xa3, 0xd6, 0x77, 0x28, \
        0x4a, 0xdd, 0xd2, 0x00, 0x12, 0x6d, 0x90, 0x69 \
}

const uint8_t expected_hash[] = EXPECTED_HASH_VALUE;
const size_t expected_hash_len = sizeof(expected_hash);

int main(void)
{
    psa_status_t status;
    uint8_t hash[PSA_HASH_LENGTH(HASH_ALG)];
    size_t hash_length;

    mbedtls_printf("PSA Crypto API: SHA-256 example\n\n");

    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        mbedtls_printf("psa_crypto_init failed\n");
        return EXIT_FAILURE;
    }

    /* Clear local variables prior to one-shot hash demo */
    memset(hash, 0, sizeof(hash));
    hash_length = 0;

    /* Compute hash using one-shot function call */
    status = psa_hash_compute(HASH_ALG,
                              sample_message, sample_message_length,
                              hash, sizeof(hash),
                              &hash_length);
    if (status != PSA_SUCCESS) {
        mbedtls_printf("psa_hash_compute failed\n");
        goto cleanup;
    }

    if (hash_length != expected_hash_len ||
        (memcmp(hash, expected_hash, expected_hash_len) != 0)) {
        mbedtls_printf("One-shot hash operation gave the wrong result!\n\n");
        goto cleanup;
    }

    mbedtls_printf("One-shot hash operation successful!\n\n");

    /* Print out result */
    mbedtls_printf("The SHA-256( '%s' ) is: ", sample_message);

    for (size_t j = 0; j < expected_hash_len; j++) {
        mbedtls_printf("%02x", hash[j]);
    }

    mbedtls_printf("\n");

    mbedtls_psa_crypto_free();
    return EXIT_SUCCESS;

cleanup:
    return EXIT_FAILURE;
}
#endif /* !MBEDTLS_PSA_CRYPTO_C || !PSA_WANT_ALG_SHA_256 */
