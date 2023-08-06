/*
 * The internal definitions
 *
 * Copyright (C) 2017-2019, Joachim Metz <joachim.metz@gmail.com>
 *
 * Refer to AUTHORS for acknowledgements.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#if !defined( LIBFCRYPTO_INTERNAL_DEFINITIONS_H )
#define LIBFCRYPTO_INTERNAL_DEFINITIONS_H

#include <common.h>
#include <types.h>

/* Define HAVE_LOCAL_LIBFCRYPTO for local use of libfcrypto
 */
#if !defined( HAVE_LOCAL_LIBFCRYPTO )
#include <libfcrypto/definitions.h>

/* The definitions in <libfcrypto/definitions.h> are copied here
 * for local use of libfcrypto
 */
#else
#include <byte_stream.h>

#define LIBFCRYPTO_VERSION			20191231

/* The version string
 */
#define LIBFCRYPTO_VERSION_STRING		"20191231"

/* The Serpent crypt modes
 */
enum LIBFCRYPTO_SERPENT_CRYPT_MODES
{
	LIBFCRYPTO_SERPENT_CRYPT_MODE_DECRYPT	= 0,
	LIBFCRYPTO_SERPENT_CRYPT_MODE_ENCRYPT	= 1
};

#endif /* !defined( HAVE_LOCAL_LIBFCRYPTO ) */

#endif /* !defined( LIBFCRYPTO_INTERNAL_DEFINITIONS_H ) */

