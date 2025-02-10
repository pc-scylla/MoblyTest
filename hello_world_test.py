#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ref: available at https://jeffhermanmobly.readthedocs.io/en/latest/tutorial.html
#   accessed 10/02/2025
#
# (pye3_11_4) PS L:\Learning\PythonProjects\MoblyTest>
#   python .\hello_world_test.py -c .\sample_config.yml
#[SampleTestBed] 02-10 22:07:42.254 INFO ==========> HelloWorldTest <==========
#[SampleTestBed] 02-10 22:07:45.371 INFO [AndroidDevice|36081FDH2004VY] Initializing the snippet package com.google.android.mobly.snippet.bundled.
#[SampleTestBed] 02-10 22:07:48.584 INFO [Test] test_hello
#[SampleTestBed] 02-10 22:07:48.601 INFO [Test] test_hello PASS
#[SampleTestBed] 02-10 22:07:49.596 INFO Summary for test class HelloWorldTest: Error 0, Executed 1, Failed 0, Passed 1, Requested 1, Skipped 0
#[SampleTestBed] 02-10 22:07:49.597 INFO Summary for test run SampleTestBed@02-10-2025_22-07-42-208:
#Total time elapsed 7.343873399775475s
#Artifacts are saved in "L:\tmp\logs\mobly\SampleTestBed\02-10-2025_22-07-42-208"
#Test summary saved in "L:\tmp\logs\mobly\SampleTestBed\02-10-2025_22-07-42-208\test_summary.yaml"
#Test results: Error 0, Executed 1, Failed 0, Passed 1, Requested 1, Skipped 0
#
from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class HelloWorldTest(base_test.BaseTestClass):
  def setup_class(self):
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at
    # least one object is created from this.
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    # Start Mobly Bundled Snippets (MBS).
    self.dut.load_snippet('mbs', 'com.google.android.mobly.snippet.bundled')

  def test_hello(self):
    self.dut.mbs.makeToast('Hello World!')


if __name__ == '__main__':
    test_runner.main()