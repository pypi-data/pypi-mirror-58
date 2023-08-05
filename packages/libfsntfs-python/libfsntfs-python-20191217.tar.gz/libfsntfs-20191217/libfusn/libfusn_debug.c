/*
 * Debug functions
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

#include <common.h>
#include <narrow_string.h>
#include <types.h>
#include <system_string.h>
#include <wide_string.h>

#include "libfusn_debug.h"
#include "libfusn_definitions.h"
#include "libfusn_libcerror.h"
#include "libfusn_libcnotify.h"
#include "libfusn_libfdatetime.h"
#include "libfusn_libuna.h"

#if defined( HAVE_DEBUG_OUTPUT )

/* Prints the update reason flags
 */
void libfusn_debug_print_update_reason_flags(
      uint32_t update_reason_flags )
{
/* TODO add description */
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_DATA_OVERWRITE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_DATA_OVERWRITE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_DATA_EXTEND ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_DATA_EXTEND)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_DATA_TRUNCATION ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_DATA_TRUNCATION)\n" );
	}

	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_NAMED_DATA_OVERWRITE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_NAMED_DATA_OVERWRITE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_NAMED_DATA_EXTEND ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_NAMED_DATA_EXTEND)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_NAMED_DATA_TRUNCATION ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_NAMED_DATA_TRUNCATION)\n" );
	}

	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_FILE_CREATE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_FILE_CREATE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_FILE_DELETE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_FILE_DELETE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_EXTENDED_ATTRIBUTE_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_EA_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_SECURITY_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_SECURITY_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_RENAME_OLD_NAME ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_RENAME_OLD_NAME)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_RENAME_NEW_NAME ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_RENAME_NEW_NAME)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_INDEXABLE_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_INDEXABLE_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_BASIC_INFO_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_BASIC_INFO_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_HARD_LINK_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_HARD_LINK_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_COMPRESSION_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_COMPRESSION_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_ENCRYPTION_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_ENCRYPTION_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_OBJECT_IDENTIFIER_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_OBJECT_IDENTIFIER_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_REPARSE_POINT_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_REPARSE_POINT_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_STREAM_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_STREAM_CHANGE)\n" );
	}
	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_TRANSACTED_CHANGE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_TRANSACTED_CHANGE)\n" );
	}

	if( ( update_reason_flags & LIBFUSN_UPDATE_REASON_FLAG_CLOSE ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_REASON_CLOSE)\n" );
	}
}

/* Prints the update source flags
 */
void libfusn_debug_print_update_source_flags(
      uint32_t update_source_flags )
{
/* TODO add description */
	if( ( update_source_flags & LIBFUSN_UPDATE_SOURCE_FLAG_DATA_MANAGEMENT ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_SOURCE_DATA_MANAGEMENT)\n" );
	}
	if( ( update_source_flags & LIBFUSN_UPDATE_SOURCE_FLAG_AUXILIARY_DATA ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_SOURCE_AUXILIARY_DATA)\n" );
	}
	if( ( update_source_flags & LIBFUSN_UPDATE_SOURCE_FLAG_REPLICATION_MANAGEMENT ) != 0 )
	{
		libcnotify_printf(
		 "\t(USN_SOURCE_REPLICATION_MANAGEMENT)\n" );
	}
}

/* Prints the file attribute flags
 */
void libfusn_debug_print_file_attribute_flags(
      uint32_t file_attribute_flags )
{
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_READ_ONLY ) != 0 )
	{
		libcnotify_printf(
		 "\tIs read-only (FILE_ATTRIBUTE_READ_ONLY)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_HIDDEN ) != 0 )
	{
		libcnotify_printf(
		 "\tIs hidden (FILE_ATTRIBUTE_HIDDEN)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_SYSTEM ) != 0 )
	{
		libcnotify_printf(
		 "\tIs system (FILE_ATTRIBUTE_SYSTEM)\n" );
	}

	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_DIRECTORY ) != 0 )
	{
		libcnotify_printf(
		 "\tIs directory (FILE_ATTRIBUTE_DIRECTORY)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_ARCHIVE ) != 0 )
	{
		libcnotify_printf(
		 "\tShould be archived (FILE_ATTRIBUTE_ARCHIVE)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_DEVICE ) != 0 )
	{
		libcnotify_printf(
		 "\tIs device (FILE_ATTRIBUTE_DEVICE)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_NORMAL ) != 0 )
	{
		libcnotify_printf(
		 "\tIs normal (FILE_ATTRIBUTE_NORMAL)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_TEMPORARY ) != 0 )
	{
		libcnotify_printf(
		 "\tIs temporary (FILE_ATTRIBUTE_TEMPORARY)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_SPARSE_FILE ) != 0 )
	{
		libcnotify_printf(
		 "\tIs a sparse file (FILE_ATTRIBUTE_SPARSE_FILE)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_REPARSE_POINT ) != 0 )
	{
		libcnotify_printf(
		 "\tIs a reparse point or symbolic link (FILE_ATTRIBUTE_FLAG_REPARSE_POINT)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_COMPRESSED ) != 0 )
	{
		libcnotify_printf(
		 "\tIs compressed (FILE_ATTRIBUTE_COMPRESSED)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_OFFLINE ) != 0 )
	{
		libcnotify_printf(
		 "\tIs offline (FILE_ATTRIBUTE_OFFLINE)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_NOT_CONTENT_INDEXED ) != 0 )
	{
		libcnotify_printf(
		 "\tContent should not be indexed (FILE_ATTRIBUTE_NOT_CONTENT_INDEXED)\n" );
	}
	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_ENCRYPTED ) != 0 )
	{
		libcnotify_printf(
		 "\tIs encrypted (FILE_ATTRIBUTE_ENCRYPTED)\n" );
	}

	if( ( file_attribute_flags & LIBFUSN_FILE_ATTRIBUTE_FLAG_VIRTUAL ) != 0 )
	{
		libcnotify_printf(
		 "\tIs virtual (FILE_ATTRIBUTE_VIRTUAL)\n" );
	}
}

/* Prints a FILETIME value
 * Returns 1 if successful or -1 on error
 */
int libfusn_debug_print_filetime_value(
     const char *function_name,
     const char *value_name,
     const uint8_t *byte_stream,
     size_t byte_stream_size,
     int byte_order,
     uint32_t string_format_flags,
     libcerror_error_t **error )
{
	char date_time_string[ 32 ];

	libfdatetime_filetime_t *filetime = NULL;
	static char *function             = "libfusn_debug_print_filetime_value";

	if( libfdatetime_filetime_initialize(
	     &filetime,
	     error ) != 1 )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_INITIALIZE_FAILED,
		 "%s: unable to create filetime.",
		 function );

		goto on_error;
	}
	if( libfdatetime_filetime_copy_from_byte_stream(
	     filetime,
	     byte_stream,
	     byte_stream_size,
	     byte_order,
	     error ) != 1 )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_COPY_FAILED,
		 "%s: unable to copy byte stream to filetime.",
		 function );

		goto on_error;
	}
	if( libfdatetime_filetime_copy_to_utf8_string(
	     filetime,
	     (uint8_t *) date_time_string,
	     32,
	     string_format_flags,
	     error ) != 1 )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_COPY_FAILED,
		 "%s: unable to copy filetime to string.",
		 function );

		goto on_error;
	}
	libcnotify_printf(
	 "%s: %s: %s UTC\n",
	 function_name,
	 value_name,
	 date_time_string );

	if( libfdatetime_filetime_free(
	     &filetime,
	     error ) != 1 )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_FINALIZE_FAILED,
		 "%s: unable to free filetime.",
		 function );

		goto on_error;
	}
	return( 1 );

on_error:
	if( filetime != NULL )
	{
		libfdatetime_filetime_free(
		 &filetime,
		 NULL );
	}
	return( -1 );
}

/* Prints an UTF-16 string value
 * Returns 1 if successful or -1 on error
 */
int libfusn_debug_print_utf16_string_value(
     const char *function_name,
     const char *value_name,
     const uint8_t *byte_stream,
     size_t byte_stream_size,
     int byte_order,
     libcerror_error_t **error )
{
	system_character_t *string = NULL;
	static char *function      = "libfusn_debug_print_utf16_string_value";
	size_t string_size         = 0;
	int result                 = 0;

	if( ( byte_stream == NULL )
	 || ( byte_stream_size == 0 ) )
	{
		libcnotify_printf(
		 "%s: %s: \n",
		 function_name,
		 value_name );

		return( 1 );
	}
#if defined( HAVE_WIDE_SYSTEM_CHARACTER )
	result = libuna_utf16_string_size_from_utf16_stream(
		  byte_stream,
		  byte_stream_size,
		  byte_order,
		  &string_size,
		  error );
#else
	result = libuna_utf8_string_size_from_utf16_stream(
		  byte_stream,
		  byte_stream_size,
		  byte_order,
		  &string_size,
		  error );
#endif
	if( result != 1 )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_GET_FAILED,
		 "%s: unable to determine size of string.",
		 function );

		goto on_error;
	}
	if( ( string_size > (size_t) SSIZE_MAX )
	 || ( ( sizeof( system_character_t ) * string_size ) > (size_t) SSIZE_MAX ) )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_VALUE_EXCEEDS_MAXIMUM,
		 "%s: invalid string size value exceeds maximum.",
		 function );

		goto on_error;
	}
	string = system_string_allocate(
	          string_size );

	if( string == NULL )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_MEMORY,
		 LIBCERROR_MEMORY_ERROR_INSUFFICIENT,
		 "%s: unable to create string.",
		 function );

		goto on_error;
	}
#if defined( HAVE_WIDE_SYSTEM_CHARACTER )
	result = libuna_utf16_string_copy_from_utf16_stream(
		  (libuna_utf16_character_t *) string,
		  string_size,
		  byte_stream,
		  byte_stream_size,
		  byte_order,
		  error );
#else
	result = libuna_utf8_string_copy_from_utf16_stream(
		  (libuna_utf8_character_t *) string,
		  string_size,
		  byte_stream,
		  byte_stream_size,
		  byte_order,
		  error );
#endif
	if( result != 1 )
	{
		libcerror_error_set(
		 error,
		 LIBCERROR_ERROR_DOMAIN_RUNTIME,
		 LIBCERROR_RUNTIME_ERROR_SET_FAILED,
		 "%s: unable to set string.",
		 function );

		goto on_error;
	}
	libcnotify_printf(
	 "%s: %s: %s\n",
	 function_name,
	 value_name,
	 string );

	memory_free(
	 string );

	return( 1 );

on_error:
	if( string != NULL )
	{
		memory_free(
		 string );
	}
	return( -1 );
}

#endif /* defined( HAVE_DEBUG_OUTPUT ) */
