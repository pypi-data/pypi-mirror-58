/*
 * Support functions
 *
 * Copyright (C) 2011-2018, Joachim Metz <joachim.metz@gmail.com>
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

#if !defined( _LIBFUSN_SUPPORT_H )
#define _LIBFUSN_SUPPORT_H

#include <common.h>
#include <types.h>

#include "libfusn_extern.h"

#if defined( __cplusplus )
extern "C" {
#endif

#if !defined( HAVE_LOCAL_LIBFUSN )

LIBFUSN_EXTERN \
const char *libfusn_get_version(
             void );

#endif

#if defined( __cplusplus )
}
#endif

#endif /* !defined( _LIBFUSN_SUPPORT_H ) */

