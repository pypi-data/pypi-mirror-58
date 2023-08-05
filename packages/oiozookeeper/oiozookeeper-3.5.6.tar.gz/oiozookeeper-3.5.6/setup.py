#  Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools
from distutils.core import setup, Extension

zookeeper_basedir = "../../"

zookeepermodule = Extension("zookeeper",
                            sources=["src/c/zookeeper.c"],
                            include_dirs=[zookeeper_basedir + "/zookeeper-client/zookeeper-client-c/include",
                                          zookeeper_basedir + "/build/c",
                                          zookeeper_basedir + "/zookeeper-client/zookeeper-client-c/generated",
                                          "/usr/include/zookeeper", "/usr/local/include/zookeeper"],
                            libraries=["zookeeper_mt"],
                            library_dirs=[zookeeper_basedir + "/zookeeper-client/zookeeper-client-c/.libs/",
                                          zookeeper_basedir + "/build/c/.libs/",
                                          zookeeper_basedir + "/build/test/test-cppunit/.libs",
                                          "/usr/local/lib"
                                          ])

descr = """
ZooKeeper Python bindings. Packaged by OpenIO to workaround naming conflicts.
"""

setup(
    name="oiozookeeper",
    version="3.5.6",
    author="Florent Vennetier",
    author_email="florent@openio.io",
    description="ZooKeeper Python bindings",
    long_description=descr,
    url="https://github.com/apache/zookeeper",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Topic :: System :: Distributed Computing",
    ],
    ext_modules=[zookeepermodule]
)
