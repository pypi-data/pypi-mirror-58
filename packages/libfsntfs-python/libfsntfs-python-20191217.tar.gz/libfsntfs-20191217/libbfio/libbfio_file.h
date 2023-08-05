/*
 * File functions
 *
 * Copyright (C) 2009-2019, Joachim Metz <joachim.metz@gmail.com>
 *
 * Refer to AUTHORS for acknowledgements.
 *
 * This software is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this software.  If not, see <http://www.gnu.org/licenses/>.
 */

#if !defined( _LIBBFIO_FILE_H )
#define _LIBBFIO_FILE_H

#include <common.h>
#include <types.h>

#include "libbfio_extern.h"
#include "libbfio_libcerror.h"
#include "libbfio_types.h"

#if defined( __cplusplus )
extern "C" {
#endif

LIBBFIO_EXTERN \
int libbfio_file_initialize(
     libbfio_handle_t **handle,
     libcerror_error_t **error );

LIBBFIO_EXTERN \
int libbfio_file_get_name_size(
     libbfio_handle_t *handle,
     size_t *name_size,
     libcerror_error_t **error );

LIBBFIO_EXTERN \
int libbfio_file_get_name(
     libbfio_handle_t *handle,
     char *name,
     size_t name_size,
     libcerror_error_t **error );

LIBBFIO_EXTERN \
int libbfio_file_set_name(
     libbfio_handle_t *handle,
     const char *name,
     size_t name_length,
     libcerror_error_t **error );

#if defined( HAVE_WIDE_CHARACTER_TYPE )

LIBBFIO_EXTERN \
int libbfio_file_get_name_size_wide(
     libbfio_handle_t *handle,
     size_t *name_size,
     libcerror_error_t **error );

LIBBFIO_EXTERN \
int libbfio_file_get_name_wide(
     libbfio_handle_t *handle,
     wchar_t *name,
     size_t name_size,
     libcerror_error_t **error );

LIBBFIO_EXTERN \
int libbfio_file_set_name_wide(
     libbfio_handle_t *handle,
     const wchar_t *name,
     size_t name_length,
     libcerror_error_t **error );

#endif /* defined( HAVE_WIDE_CHARACTER_TYPE ) */

#if defined( __cplusplus )
}
#endif

#endif /* !defined( _LIBBFIO_FILE_H ) */

