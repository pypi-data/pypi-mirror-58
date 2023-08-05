# Copyright (C) 2019 GNUnet e.V.
#
# This code is derived from code contained within build-common.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE
# LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES
# OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
# ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
# THIS SOFTWARE.
#
# This file is in the public domain.
# SPDX-License-Identifier: 0BSD

import sys
from pathlib import Path

base_dir = Path(__file__, "../build-system/taler-build-scripts").resolve()

if not base_dir.exists():
    print(f"build system directory (${base_dir}) missing", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(base_dir))

from talerbuildconfig import *

b = BuildConfig()
b.enable_prefix()
b.enable_configmk()
b.add_tool(PythonTool())
b.add_tool(PyToxTool())
b.add_tool(YapfTool())
b.add_tool(PosixTool("echo"))
b.add_tool(PosixTool("env"))
b.add_tool(PosixTool("find"))
b.add_tool(PosixTool("rm"))
b.add_tool(PosixTool("sh"))
b.add_tool(PosixTool("git"))
b.add_tool(PosixTool("xargs"))
b.run()
