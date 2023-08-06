/*
 * Copyright (C) 2019  RedNaga. https://rednaga.io
 * All rights reserved. Contact: rednaga@protonmail.com
 *
 *
 * This file is part of APKiD
 *
 *
 * Commercial License Usage
 * ------------------------
 * Licensees holding valid commercial APKiD licenses may use this file
 * in accordance with the commercial license agreement provided with the
 * Software or, alternatively, in accordance with the terms contained in
 * a written agreement between you and RedNaga.
 *
 *
 * GNU General Public License Usage
 * --------------------------------
 * Alternatively, this file may be used under the terms of the GNU General
 * Public License version 3.0 as published by the Free Software Foundation
 * and appearing in the file LICENSE.GPL included in the packaging of this
 * file. Please visit http://www.gnu.org/copyleft/gpl.html and review the
 * information to ensure the GNU General Public License version 3.0
 * requirements will be met.
 *
 **/

include "common.yara"

rule CNProtect_dex : protector
{
  // https://github.com/rednaga/APKiD/issues/52
  meta:
    description = "CNProtect (anti-disassemble)"
    sample = "5bf6887871ce5f00348b1ec6886f9dd10b5f3f5b85d3d628cf21116548a3b37d"

  strings:
    // code segment of the injected methods plus junk opcodes
    $code_segment = {
	  02 00 01 00 00 00 00 00 ?? ?? ?? ?? 11 00 00 00 00 (1? | 2? | 3? | 4? | 5? | 6? | 7? | 8? | 9? | a? | b? | c0 | c1 | c2 | c3 | c4 | c5 | c6 | c7)
    }

  condition:
    is_dex and
    $code_segment
}

rule whitecryption_dex : protector
{
  // https://github.com/rednaga/APKiD/issues/177
  meta:
    description = "WhiteCryption (dex)"
    sample      = "6821bce73b3d1146ef7ec9a2d91742a7f6fc2f8206ca9354d3d553e1b5d551a7"
    url         = "https://www.intertrust.com/products/application-shielding/"
    author      = "Tim 'diff' Strazzere"

  strings:
    // Loader class which doesnt appear to get obfuscated in these versions, plus
    // the surrounding null bytes and sizing used for the dex string table
    // Lcom/whitecryption/jcp/generated/scp;
    $loader = {
      00 25 4C 63 6F 6D 2F 77 68 69 74 65 63 72 79 70
      74 69 6F 6E 2F 6A 63 70 2F 67 65 6E 65 72 61 74
      65 64 2F 73 63 70 3B 00
    }
    // __scpClassInit with surrounding size and null bytes
    $init_stub = { 00 0E 5F 5F 73 63 70 43 6C 61 73 73 49 6E 69 74 00 }

  condition:
    is_dex and ($loader or $init_stub)
}