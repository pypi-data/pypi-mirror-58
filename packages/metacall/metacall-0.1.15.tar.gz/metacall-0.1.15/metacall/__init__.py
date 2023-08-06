#!/usr/bin/env python3

#	MetaCall Python Port by Parra Studios
#	A frontend for Python language bindings in MetaCall.
#
#	Copyright (C) 2016 - 2019 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.

import os
import sys
import re

# Append environment variable or default install path when building manually (TODO: Cross-platform paths)
sys.path.append(os.environ.get('PORT_LIBRARY_PATH', '/usr/local/lib'));

# Find is MetaCall is installed as a distributable tarball (TODO: Cross-platform paths)
rootdir = "/gnu/store/"
regex = re.compile('.*-metacall-.*')

for root, dirs, _ in os.walk(rootdir):
	for folder in dirs:
		if regex.match(folder) and not folder.endswith('R'):
			sys.path.append(os.path.join(folder, 'lib'))

try:
	from _py_port import * # TODO: Import only the functions that will be exported
except ImportError as e:
	try:
		from _py_portd import * # TODO: Import only the functions that will be exported
	except ImportError as ed:
		print("MetaCall Core is not correctly installed:", e, "-", ed)
		pass

# TODO: Monkey patch
