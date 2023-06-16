# テスティングフレームワーク
class TestCase:
  def __init__(self, name):
    self.name = name
    
  def run(self):
    method = getattr(self, self.name)
    method()
    
# テストの対象(プロダクトコード=テスティングフレームワーク)
class WasRun(TestCase):
  def __init__(self, name):
    self.wasRun = None
    super().__init__(name)
    
  def testMethod(self):
    self.wasRun = 1

# テストケース(テストコード)
class TestCaseTest(TestCase):
  def testRunning(self):
    test = WasRun("testMethod")
    assert(not test.wasRun)
    test.run()
    assert(test.wasRun)

TestCaseTest("testRunning").run()