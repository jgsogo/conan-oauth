
import shutil
from conans import ConanFile, tools, AutoToolsBuildEnvironment

class LibOauth(ConanFile):
    name = "oauth"
    version = "1.0.3"

    settings = "os", "arch", "compiler", "build_type"
    requires = "OpenSSL/1.0.2q@conan/stable"

    def source(self):
        url = "https://github.com/x42/liboauth/archive/v{}.tar.gz".format(self.version)
        tools.get(url)
        shutil.move("liboauth-{}".format(self.version), self.name)

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        with tools.environment_append(autotools.vars):
            with tools.chdir(self.name):
                self.run("autoreconf -i")
                self.run("autoconf")
                self.run("./configure --prefix={}".format(self.package_folder))
                self.run("make")
                self.run("make install")

    def package_info(self):
        self.cpp_info.libs = ["m", "curl", "crypto", "oauth"]
