from libtbx import test_utils
import libtbx.load_env

def run():
  tst_list = (
  "$D/annlib_adaptbx/sample.py",
  "$D/annlib_adaptbx/self_match.py",
  )

  build_dir = libtbx.env.under_build("annlib_adaptbx")
  dist_dir = libtbx.env.dist_path("annlib_adaptbx")

  test_utils.run_tests(build_dir, dist_dir, tst_list)

if (__name__ == "__main__"):
  run()
