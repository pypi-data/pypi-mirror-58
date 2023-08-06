#! python3
# -*- coding: utf-8 -*-

"""A Python interface to SC14N <https://www.cryptosys.net/sc14n/>."""

# $Id: sc14n.py $
# $Date: 2019-12-28 20:53:00 $

# ************************** LICENSE *****************************************
# Copyright (C) 2017-19 David Ireland, DI Management Services Pty Limited.
# <www.di-mgt.com.au> <www.cryptosys.net>
# This code is provided 'as-is' without any express or implied warranty.
# Free license is hereby granted to use this code as part of an application
# provided this license notice is left intact. You are *not* licensed to
# share any of this code in any form of mass distribution, including, but not
# limited to, reposting on other web sites or in any source code repository.
# ****************************************************************************

# Requires `Sc14n` to be installed on your system,
# available from <https://cryptosys.net/sc14n/>.

from ctypes import windll, create_string_buffer, c_char_p, c_int

__version__ = "2.1.1"
# Version 2.1.1 is version 2.1.0 converted from Python 2 to Python 3.

# OUR EXPORTED CLASSES
__all__ = (
    'C14n',
    'Tran', 'TranMethod', 'DigAlg', 'AdvOptions',
    'Gen', 'Err',
    'Error',
)

# Our global DLL object
_didll = windll.diSc14n


def _isanint(v):
    try: v = int(v)
    except: pass
    return isinstance(v, int)


class Error(Exception):
    """Raised when a call to a core library function returns an error,
    or some obviously wrong parameter is detected."""

    # Google Python Style Guide: "The base exception for a module should be called Error."

    def __init__(self, value):
        """."""
        self.value = value

    def __str__(self):
        """Behave differently if value is an integer or not."""
        if _isanint(self.value):
            n = int(self.value)
            s1 = "ERROR CODE %d: %s" % (n, Err.error_lookup(n))
        else:
            s1 = "ERROR: %s" % self.value
        se = Err.last_error()
        return "%s%s" % (s1, ": " + se if se else "")


class Gen:
    """General info about the core library DLL."""

    @staticmethod
    def version():
        """Return the release version of the core library DLL as an integer value."""
        return _didll.SC14N_Gen_Version()

    @staticmethod
    def compile_time():
        """Return date and time the core library DLL was last compiled."""
        nchars = _didll.SC14N_Gen_CompileTime(None, 0)
        buf = create_string_buffer(nchars + 1)
        nchars = _didll.SC14N_Gen_CompileTime(buf, nchars)
        return buf.value.decode()

    @staticmethod
    def module_name():
        """Return full path name of the current process's core library DLL."""
        nchars = _didll.SC14N_Gen_ModuleName(None, 0, 0)
        buf = create_string_buffer(nchars + 1)
        nchars = _didll.SC14N_Gen_ModuleName(buf, nchars, 0)
        return buf.value.decode()

    @staticmethod
    def core_platform():
        """Return the platform of the core library DLL: ``Win32`` or ``Win64``."""
        nchars = _didll.SC14N_Gen_Platform(None, 0)
        buf = create_string_buffer(nchars + 1)
        nchars = _didll.SC14N_Gen_Platform(buf, nchars)
        return buf.value.decode()[:nchars]

    @staticmethod
    def licence_type():
        """Return licence type: ``D`` = Developer ``T`` = Trial."""
        n = _didll.SC14N_Gen_LicenceType()
        return chr(n)


class Err():
    """Details of errors returned by the core library."""

    @staticmethod
    def last_error():
        """Return the last error message set by the toolkit, if any."""
        nchars = _didll.SC14N_Err_LastError(None, 0)
        buf = create_string_buffer(nchars + 1)
        nchars = _didll.SC14N_Err_LastError(buf, nchars)
        return buf.value.decode()

    @staticmethod
    def error_lookup(n):
        """Return a description of error code ``n``."""
        nchars = _didll.SC14N_Err_ErrorLookup(None, 0, c_int(n))
        buf = create_string_buffer(nchars + 1)
        nchars = _didll.SC14N_Err_ErrorLookup(buf, nchars, c_int(n))
        return buf.value.decode()


class DigAlg:
    """Message digest algorithms."""
    DEFAULT = 0       #: Use default digest algorithm.
    SHA1    = 0x0     #: Use SHA-1 digest (default)
    SHA256  = 0x2000  #: Use SHA-256 digest


class Tran:
    """Transformation options.

    **See also:** remarks for :py:func:`C14n.file2file`.
    """
    ENTIRE = 0          #: Transform the entire document.
    OMITBYTAG = 0x01    #: Omit (exclude) the element with the given tag name.
    SUBSETBYTAG = 0x02  #: Transform the subset with the given tag name.
    OMITBYID = 0x11     #: Omit (exclude) the element with the given Id.
    SUBSETBYID = 0x12   #: Transform the subset with the given Id.


class TranMethod:
    """Transformation methods."""
    INCLUSIVE = 0   #: Inclusive c14n without comments from RFC 3076 (default).
    EXCLUSIVE = 0x100   #: Exclusive c14n without comments from RFC 3741.
    INCLUSIVE_WITHCOMMENTS = 0x800  #: Inclusive C14N with comments from RFC 3076.
    EXCLUSIVE_WITHCOMMENTS = 0x900  #: Exclusive C14N with comments from RFC 3741.


class AdvOptions:
    """Advanced option flags."""
    DEFAULT = 0        #: Use default options.
    FLATTEN = 0x10000  #: Flatten the XML - remove all ignorable whitespace between tags.


class C14n:
    """Perform C14N transformation of XML document."""

    @staticmethod
    def file2file(outfile, xmlfile, nameorid="", tranopt=Tran.ENTIRE, tranmethod=TranMethod.INCLUSIVE, exclparams="", advopts=AdvOptions.DEFAULT):
        """Perform C14N transformation of XML document (file-to-file).

        Args:
            outfile (str): Name of output file to create.
            xmlfile (str): Name of input XML file.
            nameorid (str): To specify the tag name or Id.
            tranopt (Tran): Transformation option.
            tranmethod (TranMethod): Transformation method.
            exclparams (str): InclusiveNamespaces PrefixList parameter for exclusive c14n.
            advopts (AdvOptions): Advanced option flags.

        Returns:
            bool: True if successful, False otherwise.

        Remarks:
            Use the ``nameorid`` parameter to specify the element of the XML document to include or exclude.

            With options :py:const:`Tran.OMITBYTAG` or :py:const:`Tran.SUBSETBYTAG`, ``nameorid`` specifies the element's tag name.

            * By default, the first element with a matching tag name will be chosen.
            * To specify the Nth element, write as ``tagname[N]`` where ``N=1,2,3,...``

            With options :py:const:`Tran.OMITBYID` or :py:const:`Tran.SUBSETBYID`, ``nameorid`` specifies the element's Id.

            * The default Id attribute name is ``Id``, so the argument ``myvalue`` will find the element with attribute ``Id="myvalue"``.
            * To use a different attribute name - for example ``ID`` - write in the form ``ID=myvalue`` with no quotes.

            Exactly one element will be excluded or included.
            Tag names and Id values are case sensitive.
            It is an error (`NO_DATA_ERROR`) if no matching element is found.

        Examples:
            >>> # Example 1. Excludes the first element with the tag name <Signature>
            >>> r = C14n.file2file("c14nfile1.txt", "input.xml", "Signature", Tran.OMITBYTAG)
            True
            >>> # Example 2. Finds and transforms the first element with the tag name <SignedInfo>
            >>> r = C14n.file2file("c14nfile2.txt", "input.xml", "SignedInfo", Tran.SUBSETBYTAG)
            True
            >>> # Example 3. Finds and transforms the third element with the tag name <Data>
            >>> r = C14n.file2file("c14nfile3.txt", "input.xml", "Data[3]", Tran.SUBSETBYTAG)
            True
            >>> # Example 4. Finds and transforms the element with attribute Id="foo"
            >>> r = C14n.file2file("c14nfile4.txt", "input.xml", "foo", Tran.SUBSETBYID)
            True
            >>> # Example 5. Finds and transforms the element with attribute ID="bar"
            >>> r = C14n.file2file("c14nfile5.txt", "input.xml", "ID=bar", Tran.SUBSETBYID)
            True
            >>> # Example 6. Excludes element with attribute Id="thesig"
            >>> r = C14n.file2file("c14nfile6.txt", "input.xml", "thesig", Tran.OMITBYID)
            True

        """
        opts = int(tranopt) + int(tranmethod) + int(advopts)
        n = _didll.C14N_File2File(outfile.encode(), xmlfile.encode(), nameorid.encode(), exclparams.encode(), opts)
        if (n != 0): raise Error(n)
        return (n == 0)

    @staticmethod
    def file2string(xmlfile, nameorid="", tranopt=Tran.ENTIRE, tranmethod=TranMethod.INCLUSIVE, exclparams="", advopts=AdvOptions.DEFAULT):
        """Perform C14N transformation of XML document (file-to-string).

        Args:
            xmlfile (str): Name of input XML file.
            nameorid (str): To specify the tag name or Id. See remarks for :py:func:`C14n.file2file`.
            tranopt (Tran): Transformation option.
            tranmethod (TranMethod): Transformation method.
            exclparams (str): InclusiveNamespaces PrefixList parameter for exclusive c14n.
            advopts (AdvOptions): Advanced option flags.

        Returns:
            str: UTF-8-encoded string.

        """
        opts = int(tranopt) + int(tranmethod) + int(advopts)
        nc = _didll.C14N_File2String(None, 0, xmlfile.encode(), nameorid.encode(), exclparams.encode(), opts)
        if (nc < 0): raise Error(-nc)
        if (nc == 0): return ""
        buf = create_string_buffer(nc + 1)
        nc = _didll.C14N_File2String(buf, nc, xmlfile.encode(), nameorid.encode(), exclparams.encode(), opts)
        return buf.value.decode('utf-8')

    @staticmethod
    def file2digest(xmlfile, nameorid="", tranopt=Tran.ENTIRE, digalg=0, tranmethod=TranMethod.INCLUSIVE, exclparams="", advopts=AdvOptions.DEFAULT):
        """Compute digest value of C14N transformation of XML document (file-to-digest).

        Args:
            xmlfile (str): Name of input XML file.
            nameorid (str): To specify the tag name or Id. See remarks for :py:func:`C14n.file2file`.
            tranopt (Tran): Transformation option.
            digalg (DigAlg): Digest algorithm.
            tranmethod (TranMethod): Transformation method.
            exclparams (str): InclusiveNamespaces PrefixList parameter for exclusive c14n.
            advopts (AdvOptions): Advanced option flags.

        Returns:
            str: Message digest in base64-encoded string.
        """
        opts = int(tranopt) + int(tranmethod) + int(digalg) + int(advopts)   # Unexpected type warning?
        nc = _didll.C14N_File2Digest(None, 0, xmlfile.encode(), nameorid.encode(), exclparams.encode(), opts)
        if (nc < 0): raise Error(-nc)
        if (nc == 0): return ""
        buf = create_string_buffer(nc + 1)
        nc = _didll.C14N_File2Digest(buf, nc, xmlfile.encode(), nameorid.encode(), exclparams.encode(), opts)
        return buf.value.decode()

    @staticmethod
    def string2string(xmldata, nameorid="", tranopt=Tran.ENTIRE, tranmethod=TranMethod.INCLUSIVE, exclparams="", advopts=AdvOptions.DEFAULT):
        """Perform C14N transformation of XML document (string-to-string).

        Args:
            xmldata (str): XML data to be processed.
            nameorid (str): To specify the tag name or Id. See remarks for :py:func:`C14n.file2file`.
            tranopt (Tran): Transformation option.
            tranmethod (TranMethod): Transformation method.
            exclparams (str): InclusiveNamespaces PrefixList parameter for exclusive c14n.
            advopts (AdvOptions): Advanced option flags.

        Returns:
            str: UTF-8-encoded string.

        """
        opts = int(tranopt) + int(tranmethod) + int(advopts)
        d = xmldata.encode()
        nc = _didll.C14N_String2String(None, 0, d, len(d), nameorid.encode(), exclparams.encode(), opts)
        if (nc < 0): raise Error(-nc)
        if (nc == 0): return ""
        buf = create_string_buffer(nc + 1)
        nc = _didll.C14N_String2String(buf, nc, d, len(d), nameorid.encode(), exclparams.encode(), opts)
        return buf.value.decode('utf-8')

    @staticmethod
    def string2digest(xmldata, nameorid="", tranopt=Tran.ENTIRE, digalg=0, tranmethod=TranMethod.INCLUSIVE, exclparams="", advopts=AdvOptions.DEFAULT):
        """Compute digest value of C14N transformation of XML document (string-to-digest).

        Args:
            xmldata (str): XML data to be processed.
            nameorid (str): To specify the tag name or Id. See remarks for :py:func:`C14n.file2file`.
            tranopt (Tran): Transformation option.
            digalg (DigAlg): Digest algorithm.
            tranmethod (TranMethod): Transformation method.
            exclparams (str): InclusiveNamespaces PrefixList parameter for exclusive c14n.
            advopts (AdvOptions): Advanced option flags.

        Returns:
            str: Message digest in base64-encoded string.
        """
        opts = int(tranopt) + int(tranmethod) + int(digalg) + int(advopts)   # Unexpected type warning?
        d = xmldata.encode()
        nc = _didll.C14N_String2Digest(None, 0, d, len(d), nameorid.encode(), exclparams.encode(), opts)
        if (nc < 0): raise Error(-nc)
        if (nc == 0): return ""
        buf = create_string_buffer(nc + 1)
        nc = _didll.C14N_String2Digest(buf, nc, d, len(d), nameorid.encode(), exclparams.encode(), opts)
        return buf.value.decode()


class _NotUsed:
    """Dummy for parsing."""
    pass


# PROTOTYPES (derived from diSc14n.h)
# If wrong argument type is passed, these will raise an `ArgumentError` exception
#     ArgumentError: argument 1: <type 'exceptions.TypeError'>: wrong type
_didll.SC14N_Gen_Version.argtypes = []
_didll.SC14N_Gen_CompileTime.argtypes = [c_char_p, c_int]
_didll.SC14N_Gen_ModuleName.argtypes = [c_char_p, c_int, c_int]
_didll.SC14N_Gen_LicenceType.argtypes = []
_didll.SC14N_Gen_Platform.argtypes = [c_char_p, c_int]
_didll.SC14N_Err_LastError.argtypes = [c_char_p, c_int]
_didll.SC14N_Err_ErrorLookup.argtypes = [c_char_p, c_int, c_int]

_didll.C14N_File2File.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_int]
_didll.C14N_File2String.argtypes = [c_char_p, c_int, c_char_p, c_char_p, c_char_p, c_int]
_didll.C14N_File2Digest.argtypes = [c_char_p, c_int, c_char_p, c_char_p, c_char_p, c_int]
_didll.C14N_String2String.argtypes = [c_char_p, c_int, c_char_p, c_int, c_char_p, c_char_p, c_int]
_didll.C14N_String2Digest.argtypes = [c_char_p, c_int, c_char_p, c_int, c_char_p, c_char_p, c_int]
