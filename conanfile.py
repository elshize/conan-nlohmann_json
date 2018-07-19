from conans import ConanFile, CMake, tools


class NlohmannjsonConan(ConanFile):
    name = "nlohmann_json"
    version = "3.1.2"
    license = "MIT"
    url = "https://github.com/elshize/conan-nlohmann_json"
    code_url = "https://github.com/nlohmann/json"
    description = "JSON for Modern C++"
    build_policy = "always"

    def source(self):
        self.run("git clone %s --depth=1" % self.code_url)

    def package(self):
        self.copy("*.hpp", dst="include", src="json/include")
