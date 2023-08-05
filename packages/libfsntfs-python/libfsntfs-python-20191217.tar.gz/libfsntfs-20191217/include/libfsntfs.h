/*
 * Library to access the Windows NT File System (NTFS) format
 *
 * Copyright (C) 2010-2019, Joachim Metz <joachim.metz@gmail.com>
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

#if !defined( _LIBFSNTFS_H )
#define _LIBFSNTFS_H

#include <libfsntfs/codepage.h>
#include <libfsntfs/definitions.h>
#include <libfsntfs/error.h>
#include <libfsntfs/extern.h>
#include <libfsntfs/features.h>
#include <libfsntfs/types.h>

#include <stdio.h>

#if defined( LIBFSNTFS_HAVE_BFIO )
#include <libbfio.h>
#endif

#if defined( __cplusplus )
extern "C" {
#endif

/* -------------------------------------------------------------------------
 * Support functions
 * ------------------------------------------------------------------------- */

/* Returns the library version
 */
LIBFSNTFS_EXTERN \
const char *libfsntfs_get_version(
             void );

/* Returns the access flags for reading
 */
LIBFSNTFS_EXTERN \
int libfsntfs_get_access_flags_read(
     void );

/* Retrieves the narrow system string codepage
 * A value of 0 represents no codepage, UTF-8 encoding is used instead
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_get_codepage(
     int *codepage,
     libfsntfs_error_t **error );

/* Sets the narrow system string codepage
 * A value of 0 represents no codepage, UTF-8 encoding is used instead
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_set_codepage(
     int codepage,
     libfsntfs_error_t **error );

/* Determines if a file contains a NTFS volume signature
 * Returns 1 if true, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_check_volume_signature(
     const char *filename,
     libfsntfs_error_t **error );

#if defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE )

/* Determines if a file contains a NTFS volume signature
 * Returns 1 if true, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_check_volume_signature_wide(
     const wchar_t *filename,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE ) */

#if defined( LIBFSNTFS_HAVE_BFIO )

/* Determines if a file contains a NTFS volume signature using a Basic File IO (bfio) handle
 * Returns 1 if true, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_check_volume_signature_file_io_handle(
     libbfio_handle_t *file_io_handle,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_BFIO ) */

/* Determines if a file contains a NTFS MFT metadata file signature
 * Returns 1 if true, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_check_mft_metadata_file_signature(
     const char *filename,
     libfsntfs_error_t **error );

#if defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE )

/* Determines if a file contains a NTFS MFT metadata file signature
 * Returns 1 if true, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_check_mft_metadata_file_signature_wide(
     const wchar_t *filename,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE ) */

#if defined( LIBFSNTFS_HAVE_BFIO )

/* Determines if a file contains a NTFS MFT metadata file signature using a Basic File IO (bfio) handle
 * Returns 1 if true, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_check_mft_metadata_file_signature_file_io_handle(
     libbfio_handle_t *file_io_handle,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_BFIO ) */

/* -------------------------------------------------------------------------
 * Notify functions
 * ------------------------------------------------------------------------- */

/* Sets the verbose notification
 */
LIBFSNTFS_EXTERN \
void libfsntfs_notify_set_verbose(
      int verbose );

/* Sets the notification stream
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_notify_set_stream(
     FILE *stream,
     libfsntfs_error_t **error );

/* Opens the notification stream using a filename
 * The stream is opened in append mode
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_notify_stream_open(
     const char *filename,
     libfsntfs_error_t **error );

/* Closes the notification stream if opened using a filename
 * Returns 0 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_notify_stream_close(
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * Error functions
 * ------------------------------------------------------------------------- */

/* Frees an error
 */
LIBFSNTFS_EXTERN \
void libfsntfs_error_free(
      libfsntfs_error_t **error );

/* Prints a descriptive string of the error to the stream
 * Returns the number of printed characters if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_error_fprint(
     libfsntfs_error_t *error,
     FILE *stream );

/* Prints a descriptive string of the error to the string
 * The end-of-string character is not included in the return value
 * Returns the number of printed characters if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_error_sprint(
     libfsntfs_error_t *error,
     char *string,
     size_t size );

/* Prints a backtrace of the error to the stream
 * Returns the number of printed characters if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_error_backtrace_fprint(
     libfsntfs_error_t *error,
     FILE *stream );

/* Prints a backtrace of the error to the string
 * The end-of-string character is not included in the return value
 * Returns the number of printed characters if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_error_backtrace_sprint(
     libfsntfs_error_t *error,
     char *string,
     size_t size );

/* -------------------------------------------------------------------------
 * Volume functions
 * ------------------------------------------------------------------------- */

/* Creates a volume
 * Make sure the value volume is referencing, is set to NULL
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_initialize(
     libfsntfs_volume_t **volume,
     libfsntfs_error_t **error );

/* Frees a volume
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_free(
     libfsntfs_volume_t **volume,
     libfsntfs_error_t **error );

/* Signals the volume to abort its current activity
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_signal_abort(
     libfsntfs_volume_t *volume,
     libfsntfs_error_t **error );

/* Opens a volume
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_open(
     libfsntfs_volume_t *volume,
     const char *filename,
     int access_flags,
     libfsntfs_error_t **error );

#if defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE )

/* Opens a volume
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_open_wide(
     libfsntfs_volume_t *volume,
     const wchar_t *filename,
     int access_flags,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE ) */

#if defined( LIBFSNTFS_HAVE_BFIO )

/* Opens a volume using a Basic File IO (bfio) handle
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_open_file_io_handle(
     libfsntfs_volume_t *volume,
     libbfio_handle_t *file_io_handle,
     int access_flags,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_BFIO ) */

/* Closes a volume
 * Returns 0 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_close(
     libfsntfs_volume_t *volume,
     libfsntfs_error_t **error );

/* Determines if the volume has BitLocker Drive Encryption (BDE)
 * Returns 1 if the volume has BitLocker Drive Encryption, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_has_bitlocker_drive_encryption(
     libfsntfs_volume_t *volume,
     libfsntfs_error_t **error );

/* Determines if the volume has Volume Shadow Snapshots (VSS)
 * Returns 1 if the volume has Volume Shadow Snapshots, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_has_volume_shadow_snapshots(
     libfsntfs_volume_t *volume,
     libfsntfs_error_t **error );

/* Retrieves the bytes per sector
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_bytes_per_sector(
     libfsntfs_volume_t *volume,
     uint16_t *bytes_per_sector,
     libfsntfs_error_t **error );

/* Retrieves the cluster block size
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_cluster_block_size(
     libfsntfs_volume_t *volume,
     size32_t *cluster_block_size,
     libfsntfs_error_t **error );

/* Retrieves the MFT entry size
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_mft_entry_size(
     libfsntfs_volume_t *volume,
     size32_t *mft_entry_size,
     libfsntfs_error_t **error );

/* Retrieves the index entry size
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_index_entry_size(
     libfsntfs_volume_t *volume,
     size32_t *index_entry_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded name
 * The returned size includes the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_utf8_name_size(
     libfsntfs_volume_t *volume,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name
 * The size should include the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_utf8_name(
     libfsntfs_volume_t *volume,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name
 * The returned size includes the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_utf16_name_size(
     libfsntfs_volume_t *volume,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name
 * The size should include the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_utf16_name(
     libfsntfs_volume_t *volume,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the version
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_version(
     libfsntfs_volume_t *volume,
     uint8_t *major_version,
     uint8_t *minor_version,
     libfsntfs_error_t **error );

/* Retrieves the serial number
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_serial_number(
     libfsntfs_volume_t *volume,
     uint64_t *serial_number,
     libfsntfs_error_t **error );

/* Retrieves the number of file entries (MFT entries)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_number_of_file_entries(
     libfsntfs_volume_t *volume,
     uint64_t *number_of_file_entries,
     libfsntfs_error_t **error );

/* Retrieves the file entry of a specific MFT entry index
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_file_entry_by_index(
     libfsntfs_volume_t *volume,
     uint64_t mft_entry_index,
     libfsntfs_file_entry_t **file_entry,
     libfsntfs_error_t **error );

/* Retrieves the file entry for an UTF-8 encoded path
 * Returns 1 if successful, 0 if no such file entry or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_file_entry_by_utf8_path(
     libfsntfs_volume_t *volume,
     const uint8_t *utf8_string,
     size_t utf8_string_length,
     libfsntfs_file_entry_t **file_entry,
     libfsntfs_error_t **error );

/* Retrieves the file entry for an UTF-16 encoded path
 * Returns 1 if successful, 0 if no such file entry or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_file_entry_by_utf16_path(
     libfsntfs_volume_t *volume,
     const uint16_t *utf16_string,
     size_t utf16_string_length,
     libfsntfs_file_entry_t **file_entry,
     libfsntfs_error_t **error );

/* Retrieves the root directory file entry
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_root_directory(
     libfsntfs_volume_t *volume,
     libfsntfs_file_entry_t **file_entry,
     libfsntfs_error_t **error );

/* Retrieves the usn change journal
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_get_usn_change_journal(
     libfsntfs_volume_t *volume,
     libfsntfs_usn_change_journal_t **usn_change_journal,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * File entry functions
 * ------------------------------------------------------------------------- */

/* Frees a file entry
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_free(
     libfsntfs_file_entry_t **file_entry,
     libfsntfs_error_t **error );

/* Determines if the file entry is emtpy
 * Returns 1 if empty, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_is_empty(
     libfsntfs_file_entry_t *file_entry,
     libfsntfs_error_t **error );

/* Determines if the file entry is allocated (MFT entry in use flag is set)
 * Returns 1 if allocated, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_is_allocated(
     libfsntfs_file_entry_t *file_entry,
     libfsntfs_error_t **error );

/* Retrieves the file reference
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_file_reference(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *file_reference,
     libfsntfs_error_t **error );

/* Retrieves the base record file reference
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_base_record_file_reference(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *file_reference,
     libfsntfs_error_t **error );

/* Retrieves the parent file reference
 * This value is retrieved from the directory entry $FILE_NAME attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_parent_file_reference(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *parent_file_reference,
     libfsntfs_error_t **error );

/* Retrieves the parent file reference for a specific $FILE_NAME attribute
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_parent_file_reference_by_attribute_index(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     uint64_t *parent_file_reference,
     libfsntfs_error_t **error );

/* Retrieves the journal sequence number
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_journal_sequence_number(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *journal_sequence_number,
     libfsntfs_error_t **error );

/* Retrieves the creation date and time
 * This value is retrieved from the $STANDARD_INFORMATION attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_creation_time(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the modification date and time
 * This value is retrieved from the $STANDARD_INFORMATION attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_modification_time(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the access date and time
 * This value is retrieved from the $STANDARD_INFORMATION attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_access_time(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the entry modification date and time
 * This value is retrieved from the $STANDARD_INFORMATION attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_entry_modification_time(
     libfsntfs_file_entry_t *file_entry,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the file attribute flags
 * This value is retrieved from the $STANDARD_INFORMATION attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_file_attribute_flags(
     libfsntfs_file_entry_t *file_entry,
     uint32_t *file_attribute_flags,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded name
 * The returned size includes the end of string character
 * This value is retrieved from the directory entry $FILE_NAME attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_name_size(
     libfsntfs_file_entry_t *file_entry,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name
 * The size should include the end of string character
 * This value is retrieved from the directory entry $FILE_NAME attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_name(
     libfsntfs_file_entry_t *file_entry,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name
 * The returned size includes the end of string character
 * This value is retrieved from the directory entry $FILE_NAME attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_name_size(
     libfsntfs_file_entry_t *file_entry,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name
 * The size should include the end of string character
 * This value is retrieved from the directory entry $FILE_NAME attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_name(
     libfsntfs_file_entry_t *file_entry,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the name attribute index
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_name_attribute_index(
     libfsntfs_file_entry_t *file_entry,
     int *attribute_index,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded name for a specific $FILE_NAME attribute
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_name_size_by_attribute_index(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name for a specific $FILE_NAME attribute
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_name_by_attribute_index(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name for a specific $FILE_NAME attribute
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_name_size_by_attribute_index(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name for a specific $FILE_NAME attribute
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_name_by_attribute_index(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded path hint for a specific $FILE_NAME attribute
 * The returned size includes the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_path_hint_size(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded path hint for a specific $FILE_NAME attribute
 * The size should include the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_path_hint(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded path hint for a specific $FILE_NAME attribute
 * The returned size includes the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_path_hint_size(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded path hint for a specific $FILE_NAME attribute
 * The size should include the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_path_hint(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded symbolic link target
 * The returned size includes the end of string character
 * This value is retrieved from a symbolic link $REPARSE_POINT attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_symbolic_link_target_size(
     libfsntfs_file_entry_t *file_entry,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded symbolic link target
 * The size should include the end of string character
 * This value is retrieved from a symbolic link $REPARSE_POINT attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf8_symbolic_link_target(
     libfsntfs_file_entry_t *file_entry,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded symbolic link target
 * The returned size includes the end of string character
 * This value is retrieved from a symbolic link $REPARSE_POINT attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_symbolic_link_target_size(
     libfsntfs_file_entry_t *file_entry,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded symbolic link target
 * The size should include the end of string character
 * This value is retrieved from a symbolic link $REPARSE_POINT attribute
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_utf16_symbolic_link_target(
     libfsntfs_file_entry_t *file_entry,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the security descriptor (data) size
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_security_descriptor_size(
     libfsntfs_file_entry_t *file_entry,
     size_t *data_size,
     libfsntfs_error_t **error );

/* Retrieves the security descriptor (data)
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_security_descriptor(
     libfsntfs_file_entry_t *file_entry,
     uint8_t *data,
     size_t data_size,
     libfsntfs_error_t **error );

/* Retrieves the number of attributes
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_number_of_attributes(
     libfsntfs_file_entry_t *file_entry,
     int *number_of_attributes,
     libfsntfs_error_t **error );

/* Retrieves the attribute for the specific index
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_attribute_by_index(
     libfsntfs_file_entry_t *file_entry,
     int attribute_index,
     libfsntfs_attribute_t **attribute,
     libfsntfs_error_t **error );

/* Determines if the file entry has the directory entries ($I30) index
 * Returns 1 if the file entry has a directory entries index, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_has_directory_entries_index(
     libfsntfs_file_entry_t *file_entry,
     libfsntfs_error_t **error );

/* Determines if the file entry has the default data stream (nameless $DATA attribute)
 * Returns 1 if the file entry has a default data stream, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_has_default_data_stream(
     libfsntfs_file_entry_t *file_entry,
     libfsntfs_error_t **error );

/* Determines if the file entry is a symbolic link
 * Returns 1 if the file entry is a symbolic link, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_is_symbolic_link(
     libfsntfs_file_entry_t *file_entry,
     libfsntfs_error_t **error );

/* Retrieves the number of alternate data streams
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_number_of_alternate_data_streams(
     libfsntfs_file_entry_t *file_entry,
     int *number_of_alternate_data_streams,
     libfsntfs_error_t **error );

/* Retrieves the alternate data stream for the specific index
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_alternate_data_stream_by_index(
     libfsntfs_file_entry_t *file_entry,
     int alternate_data_stream_index,
     libfsntfs_data_stream_t **alternate_data_stream,
     libfsntfs_error_t **error );

/* Determines if there is an alternate data stream for an UTF-8 encoded name
 * Returns 1 if available, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_has_alternate_data_stream_by_utf8_name(
     libfsntfs_file_entry_t *file_entry,
     const uint8_t *utf8_string,
     size_t utf8_string_length,
     libfsntfs_error_t **error );

/* Determines if there is an alternate data stream for an UTF-16 encoded name
 * Returns 1 if available, 0 if not or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_has_alternate_data_stream_by_utf16_name(
     libfsntfs_file_entry_t *file_entry,
     const uint16_t *utf16_string,
     size_t utf16_string_length,
     libfsntfs_error_t **error );

/* Retrieves the alternate data stream for an UTF-8 encoded name
 * Returns 1 if successful, 0 if the file entry does not contain such value or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_alternate_data_stream_by_utf8_name(
     libfsntfs_file_entry_t *file_entry,
     const uint8_t *utf8_string,
     size_t utf8_string_length,
     libfsntfs_data_stream_t **alternate_data_stream,
     libfsntfs_error_t **error );

/* Retrieves the alternate data stream for an UTF-16 encoded name
 * Returns 1 if successful, 0 if the file entry does not contain such value or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_alternate_data_stream_by_utf16_name(
     libfsntfs_file_entry_t *file_entry,
     const uint16_t *utf16_string,
     size_t utf16_string_length,
     libfsntfs_data_stream_t **alternate_data_stream,
     libfsntfs_error_t **error );

/* Retrieves the number of sub file entries
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_number_of_sub_file_entries(
     libfsntfs_file_entry_t *file_entry,
     int *number_of_sub_file_entries,
     libfsntfs_error_t **error );

/* Retrieves the sub file entry for the specific index
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_sub_file_entry_by_index(
     libfsntfs_file_entry_t *file_entry,
     int sub_file_entry_index,
     libfsntfs_file_entry_t **sub_file_entry,
     libfsntfs_error_t **error );

/* Retrieves the sub file entry for an UTF-8 encoded name
 * Returns 1 if successful, 0 if the file entry does not contain such value or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_sub_file_entry_by_utf8_name(
     libfsntfs_file_entry_t *file_entry,
     const uint8_t *utf8_string,
     size_t utf8_string_length,
     libfsntfs_file_entry_t **sub_file_entry,
     libfsntfs_error_t **error );

/* Retrieves the sub file entry for an UTF-16 encoded name
 * Returns 1 if successful, 0 if the file entry does not contain such value or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_sub_file_entry_by_utf16_name(
     libfsntfs_file_entry_t *file_entry,
     const uint16_t *utf16_string,
     size_t utf16_string_length,
     libfsntfs_file_entry_t **sub_file_entry,
     libfsntfs_error_t **error );

/* Reads data at the current offset from the default data stream (nameless $DATA attribute)
 * Returns the number of bytes read or -1 on error
 */
LIBFSNTFS_EXTERN \
ssize_t libfsntfs_file_entry_read_buffer(
         libfsntfs_file_entry_t *file_entry,
         void *buffer,
         size_t buffer_size,
         libfsntfs_error_t **error );

/* Reads data at a specific offset from the default data stream (nameless $DATA attribute)
 * Returns the number of bytes read or -1 on error
 */
LIBFSNTFS_EXTERN \
ssize_t libfsntfs_file_entry_read_buffer_at_offset(
         libfsntfs_file_entry_t *file_entry,
         void *buffer,
         size_t buffer_size,
         off64_t offset,
         libfsntfs_error_t **error );

/* Seeks a certain offset of in the default data stream (nameless $DATA attribute)
 * Returns the offset if seek is successful or -1 on error
 */
LIBFSNTFS_EXTERN \
off64_t libfsntfs_file_entry_seek_offset(
         libfsntfs_file_entry_t *file_entry,
         off64_t offset,
         int whence,
         libfsntfs_error_t **error );

/* Retrieves the current offset of the default data stream (nameless $DATA attribute)
 * Returns the offset if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_offset(
     libfsntfs_file_entry_t *file_entry,
     off64_t *offset,
     libfsntfs_error_t **error );

/* Retrieves the size of the default data stream (nameless $DATA attribute)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_size(
     libfsntfs_file_entry_t *file_entry,
     size64_t *size,
     libfsntfs_error_t **error );

/* Retrieves the number of extents (decoded data runs) of the default data stream (nameless $DATA attribute)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_number_of_extents(
     libfsntfs_file_entry_t *file_entry,
     int *number_of_extents,
     libfsntfs_error_t **error );

/* Retrieves a specific extent (decoded data run) of the default data stream (nameless $DATA attribute)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_entry_get_extent_by_index(
     libfsntfs_file_entry_t *file_entry,
     int extent_index,
     off64_t *extent_offset,
     size64_t *extent_size,
     uint32_t *extent_flags,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * Attribute functions
 * ------------------------------------------------------------------------- */

/* Frees an attribute
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_free(
     libfsntfs_attribute_t **attribute,
     libfsntfs_error_t **error );

/* Retrieves the type
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_type(
     libfsntfs_attribute_t *attribute,
     uint32_t *type,
     libfsntfs_error_t **error );

/* Retrieves the data flags
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_data_flags(
     libfsntfs_attribute_t *attribute,
     uint16_t *data_flags,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_utf8_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_utf8_name(
     libfsntfs_attribute_t *attribute,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_utf16_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_utf16_name(
     libfsntfs_attribute_t *attribute,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the data VCN range
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_data_vcn_range(
     libfsntfs_attribute_t *attribute,
     uint64_t *data_first_vcn,
     uint64_t *data_last_vcn,
     libfsntfs_error_t **error );

/* Retrieves the file references as an MFT entry index and sequence number
 * If the value sequence_number is NULL it will be ignored
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_file_reference(
     libfsntfs_attribute_t *attribute,
     uint64_t *mft_entry_index,
     uint16_t *sequence_number,
     libfsntfs_error_t **error );

/* Retrieves the data size
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_attribute_get_data_size(
     libfsntfs_attribute_t *attribute,
     size64_t *data_size,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $FILE_NAME attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the parent file reference
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_parent_file_reference(
     libfsntfs_attribute_t *attribute,
     uint64_t *parent_file_reference,
     libfsntfs_error_t **error );

/* Retrieves the creation date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_creation_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the modification date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_modification_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the access date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_access_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the entry modification date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_entry_modification_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the file attribute flags
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_file_attribute_flags(
     libfsntfs_attribute_t *attribute,
     uint32_t *file_attribute_flags,
     libfsntfs_error_t **error );

/* Retrieves the namespace
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_namespace(
     libfsntfs_attribute_t *attribute,
     uint8_t *namespace,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_utf8_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_utf8_name(
     libfsntfs_attribute_t *attribute,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_utf16_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_file_name_attribute_get_utf16_name(
     libfsntfs_attribute_t *attribute,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $OBJECT_ID attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the droid file identifier
 * Returns 1 if successful or -1 on error
 */
int libfsntfs_object_identifier_attribute_get_droid_file_identifier(
     libfsntfs_attribute_t *attribute,
     uint8_t *guid,
     size_t size,
     libfsntfs_error_t **error );

/* Retrieves the birth droid volume identifier
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_object_identifier_attribute_get_birth_droid_volume_identifier(
     libfsntfs_attribute_t *attribute,
     uint8_t *guid,
     size_t size,
     libfsntfs_error_t **error );

/* Retrieves the birth droid file identifier
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_object_identifier_attribute_get_birth_droid_file_identifier(
     libfsntfs_attribute_t *attribute,
     uint8_t *guid,
     size_t size,
     libfsntfs_error_t **error );

/* Retrieves the birth droid domain identifier
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_object_identifier_attribute_get_birth_droid_domain_identifier(
     libfsntfs_attribute_t *attribute,
     uint8_t *guid,
     size_t size,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $REPARSE_POINT attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the type and flags
 * The tag is a combination of the type and flags
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_reparse_point_attribute_get_tag(
     libfsntfs_attribute_t *attribute,
     uint32_t *tag,
     libfsntfs_error_t **error );

/* Retrieves the Windows Overlay Filter (WOF) compression_method
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_compression_method(
     libfsntfs_attribute_t *attribute,
     uint32_t *compression_method,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded substitute name
 * The returned size includes the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf8_substitute_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded substitute name
 * The size should include the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf8_substitute_name(
     libfsntfs_attribute_t *attribute,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded substitute name
 * The returned size includes the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf16_substitute_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded substitute name
 * The size should include the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf16_substitute_name(
     libfsntfs_attribute_t *attribute,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded print name
 * The returned size includes the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf8_print_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded print name
 * The size should include the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf8_print_name(
     libfsntfs_attribute_t *attribute,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded print name
 * The returned size includes the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf16_print_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded print name
 * The size should include the end of string character
 * Returns 1 if successful, 0 if not available or -1 on error
 */
int libfsntfs_reparse_point_attribute_get_utf16_print_name(
     libfsntfs_attribute_t *attribute,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $SECURITY_DESCRIPTOR attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the security descriptor (data) size
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_security_descriptor_attribute_get_security_descriptor_size(
     libfsntfs_attribute_t *attribute,
     size_t *data_size,
     libfsntfs_error_t **error );

/* Retrieves the security descriptor (data)
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_security_descriptor_attribute_get_security_descriptor(
     libfsntfs_attribute_t *attribute,
     uint8_t *data,
     size_t data_size,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $STANDARD_INFORMATION attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the creation date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_creation_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the modification date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_modification_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the access date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_access_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the entry modification date and time
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_entry_modification_time(
     libfsntfs_attribute_t *attribute,
     uint64_t *filetime,
     libfsntfs_error_t **error );

/* Retrieves the file attribute flags
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_file_attribute_flags(
     libfsntfs_attribute_t *attribute,
     uint32_t *file_attribute_flags,
     libfsntfs_error_t **error );

/* Retrieves the owner identifier
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_owner_identifier(
     libfsntfs_attribute_t *attribute,
     uint32_t *owner_identifier,
     libfsntfs_error_t **error );

/* Retrieves the security descriptor identifier
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_security_descriptor_identifier(
     libfsntfs_attribute_t *attribute,
     uint32_t *security_descriptor_identifier,
     libfsntfs_error_t **error );

/* Retrieves the update sequence number (USN)
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_standard_information_attribute_get_update_sequence_number(
     libfsntfs_attribute_t *attribute,
     uint64_t *update_sequence_number,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $VOLUME_INFORMATION attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the version
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_information_attribute_get_version(
     libfsntfs_attribute_t *attribute,
     uint8_t *major_version,
     uint8_t *minor_version,
     libfsntfs_error_t **error );

/* Retrieves the flags
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_information_attribute_get_flags(
     libfsntfs_attribute_t *attribute,
     uint16_t *flags,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * $VOLUME_NAME attribute functions
 * ------------------------------------------------------------------------- */

/* Retrieves the size of the UTF-8 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_name_attribute_get_utf8_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_name_attribute_get_utf8_name(
     libfsntfs_attribute_t *attribute,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_name_attribute_get_utf16_name_size(
     libfsntfs_attribute_t *attribute,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_volume_name_attribute_get_utf16_name(
     libfsntfs_attribute_t *attribute,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * Data stream functions
 * ------------------------------------------------------------------------- */

/* Frees an data stream
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_free(
     libfsntfs_data_stream_t **data_stream,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_utf8_name_size(
     libfsntfs_data_stream_t *data_stream,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_utf8_name(
     libfsntfs_data_stream_t *data_stream,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded name
 * The returned size includes the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_utf16_name_size(
     libfsntfs_data_stream_t *data_stream,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded name
 * The size should include the end of string character
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_utf16_name(
     libfsntfs_data_stream_t *data_stream,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Reads data at the current offset
 * Returns the number of bytes read or -1 on error
 */
LIBFSNTFS_EXTERN \
ssize_t libfsntfs_data_stream_read_buffer(
         libfsntfs_data_stream_t *data_stream,
         void *buffer,
         size_t buffer_size,
         libfsntfs_error_t **error );

/* Reads data at a specific offset
 * Returns the number of bytes read or -1 on error
 */
LIBFSNTFS_EXTERN \
ssize_t libfsntfs_data_stream_read_buffer_at_offset(
         libfsntfs_data_stream_t *data_stream,
         void *buffer,
         size_t buffer_size,
         off64_t offset,
         libfsntfs_error_t **error );

/* Seeks a certain offset of the data
 * Returns the offset if seek is successful or -1 on error
 */
LIBFSNTFS_EXTERN \
off64_t libfsntfs_data_stream_seek_offset(
         libfsntfs_data_stream_t *data_stream,
         off64_t offset,
         int whence,
         libfsntfs_error_t **error );

/* Retrieves the current offset of the data
 * Returns the offset if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_offset(
     libfsntfs_data_stream_t *data_stream,
     off64_t *offset,
     libfsntfs_error_t **error );

/* Retrieves the size
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_size(
     libfsntfs_data_stream_t *data_stream,
     size64_t *size,
     libfsntfs_error_t **error );

/* Retrieves the number of extents (decoded data runs)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_number_of_extents(
     libfsntfs_data_stream_t *data_stream,
     int *number_of_extents,
     libfsntfs_error_t **error );

/* Retrieves a specific extent (decoded data run)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_data_stream_get_extent_by_index(
     libfsntfs_data_stream_t *data_stream,
     int extent_index,
     off64_t *extent_offset,
     size64_t *extent_size,
     uint32_t *extent_flags,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * MFT metadata file functions
 * ------------------------------------------------------------------------- */

/* Creates a MFT metadata file
 * Make sure the value mft_metadata_file is referencing, is set to NULL
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_initialize(
     libfsntfs_mft_metadata_file_t **mft_metadata_file,
     libfsntfs_error_t **error );

/* Frees a MFT metadata file
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_free(
     libfsntfs_mft_metadata_file_t **mft_metadata_file,
     libfsntfs_error_t **error );

/* Opens a MFT metadata file
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_open(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     const char *filename,
     int access_flags,
     libfsntfs_error_t **error );

#if defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE )

/* Opens a MFT metadata file
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_open_wide(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     const wchar_t *filename,
     int access_flags,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_WIDE_CHARACTER_TYPE ) */

#if defined( LIBFSNTFS_HAVE_BFIO )

/* Opens a MFT metadata file using a Basic File IO (bfio) handle
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_open_file_io_handle(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     libbfio_handle_t *file_io_handle,
     int access_flags,
     libfsntfs_error_t **error );

#endif /* defined( LIBFSNTFS_HAVE_BFIO ) */

/* Closes a MFT metadata file
 * Returns 0 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_close(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-8 encoded volume name
 * The returned size includes the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_utf8_volume_name_size(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     size_t *utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-8 encoded volume name
 * The size should include the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_utf8_volume_name(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     uint8_t *utf8_string,
     size_t utf8_string_size,
     libfsntfs_error_t **error );

/* Retrieves the size of the UTF-16 encoded volume name
 * The returned size includes the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_utf16_volume_name_size(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     size_t *utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the UTF-16 encoded volume name
 * The size should include the end of string character
 * This value is retrieved from the $VOLUME_NAME attribute of the $Volume metadata file
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_utf16_volume_name(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     uint16_t *utf16_string,
     size_t utf16_string_size,
     libfsntfs_error_t **error );

/* Retrieves the volume version
 * Returns 1 if successful, 0 if not available or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_volume_version(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     uint8_t *major_version,
     uint8_t *minor_version,
     libfsntfs_error_t **error );

/* Retrieves the number of file entries (MFT entries)
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_number_of_file_entries(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     uint64_t *number_of_file_entries,
     libfsntfs_error_t **error );

/* Retrieves the file entry of a specific MFT entry index
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_mft_metadata_file_get_file_entry_by_index(
     libfsntfs_mft_metadata_file_t *mft_metadata_file,
     uint64_t mft_entry_index,
     libfsntfs_file_entry_t **file_entry,
     libfsntfs_error_t **error );

/* -------------------------------------------------------------------------
 * USN change journal functions
 * ------------------------------------------------------------------------- */

/* Frees an USN change journal
 * Returns 1 if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_usn_change_journal_free(
     libfsntfs_usn_change_journal_t **usn_change_journal,
     libfsntfs_error_t **error );

/* Retrieves the current offset of the USN change journal
 * Returns the offset if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
int libfsntfs_usn_change_journal_get_offset(
     libfsntfs_usn_change_journal_t *usn_change_journal,
     off64_t *offset,
     libfsntfs_error_t **error );

/* Reads an USN record from the USN change journal
 * Returns the number of bytes read if successful or -1 on error
 */
LIBFSNTFS_EXTERN \
ssize_t libfsntfs_usn_change_journal_read_usn_record(
         libfsntfs_usn_change_journal_t *usn_change_journal,
         uint8_t *usn_record_data,
         size_t usn_record_data_size,
         libfsntfs_error_t **error );

#if defined( __cplusplus )
}
#endif

#endif /* !defined( _LIBFSNTFS_H ) */

