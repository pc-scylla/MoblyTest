# Small test to Wifi Enable Test
#
# To use these snippets within Mobly tests, load it on your AndroidDevice objects 
# after registering android_device module:
#
# Test carried out
# ================
# (pye3_11_4) PS L:\Learning\PythonProjects\mobly\tools> 
#   python snippet_shell.py com.google.android.mobly.snippet.bundled -s 36081FDH2004VY
#   python snippet_shell.py com.google.android.mobly.snippet.bundled -s 3A131JEHN06720
#
#(pye3_11_4) PS L:\Learning\PythonProjects\MoblyTest> python .\wifi_test.py -c .\pixel7_config.yml --test_case test_start test_wifi test_end
#[SampleTestBed] 02-10 21:46:34.744 INFO ==========> WifiEnabledTest <==========
#[SampleTestBed] 02-10 21:46:37.873 INFO [AndroidDevice|36081FDH2004VY] Initializing the snippet package com.google.android.mobly.snippet.bundled.
#[SampleTestBed] 02-10 21:46:41.172 INFO [AndroidDevice|3A131JEHN06720] Initializing the snippet package com.google.android.mobly.snippet.bundled.2
#[SampleTestBed] 02-10 21:46:44.431 INFO [Test] test_start
#[SampleTestBed] 02-10 21:46:44.479 INFO [Test] test_start PASS
#[SampleTestBed] 02-10 21:46:44.482 INFO [Test] test_wifi
#
#self.dut: <AndroidDevice|36081FDH2004VY>
#s: <mobly.controllers.android_device_lib.snippet_client_v2.SnippetClientV2 object at 0x000002A6CB13A750>
#
#s.wifiIsApEnabled(): False
#s.isWifiConnected(): True
#
#self.dut: <AndroidDevice|3A131JEHN06720>
#s: <mobly.controllers.android_device_lib.snippet_client_v2.SnippetClientV2 object at 0x000001F3B307CC50>
#
#s.wifiIsApEnabled(): False
#s.isWifiConnected(): False
#test_wifi COMPLETED
#[SampleTestBed] 02-10 21:46:44.615 INFO [Test] test_wifi PASS
#[SampleTestBed] 02-10 21:46:44.622 INFO [Test] test_end
#[SampleTestBed] 02-10 21:46:44.645 INFO [Test] test_end PASS
#[SampleTestBed] 02-10 21:46:46.408 INFO Summary for test class WifiEnabledTest: Error 0, Executed 3, Failed 0, Passed 3, Requested 3, Skipped 0
#[SampleTestBed] 02-10 21:46:46.409 INFO Summary for test run SampleTestBed@02-10-2025_21-46-34-695:
#Total time elapsed 11.665505999932066s
#Artifacts are saved in "L:\tmp\logs\mobly\SampleTestBed\02-10-2025_21-46-34-695"
#Test summary saved in "L:\tmp\logs\mobly\SampleTestBed\02-10-2025_21-46-34-695\test_summary.yaml"
#Test results: Error 0, Executed 3, Failed 0, Passed 3, Requested 3, Skipped 0
#

import argparse
import logging
import sys
from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class WifiEnabledTest(base_test.BaseTestClass):
  
  def setup_class(self):
    import traceback
    import logging
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at
    # least one object is created from this.
    self.ads = []
    try:
        self.ads = self.register_controller(android_device)

    except Exception as e:
        logging.error(traceback.format_exc())
        # Logs the error appropriately. 
        print (e)
       
    self.dut = []
    for i in range (len(self.ads)):
        self.dut.append(self.ads[i])            
        # Start Mobly Bundled Snippets (MBS).
        self.dut[i].load_snippet('mbs', 'com.google.android.mobly.snippet.bundled')    
    else:
       print(len(self.ads))
  
  def test_start(self):
    for dut in self.dut:
        dut.mbs.makeToast('Start Wifi Enabled Test!')

  def test_end(self):
    for dut in self.dut:
        dut.mbs.makeToast('End test Goodbye!')

  def test_wifi(self):
    for dut in self.dut:
        s = dut.mbs
        print(f"\nself.dut: {dut}")
        print(f"s: {s}\n")
        ApRes = s.wifiIsApEnabled()
        print(f"s.wifiIsApEnabled(): {ApRes}")
        WifiRef = s.isWifiConnected()
        print(f"s.isWifiConnected(): {WifiRef}")
    else:
       print("test_wifi COMPLETED")

if __name__ == '__main__':
    test_runner.main()