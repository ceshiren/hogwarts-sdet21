## 霍格沃兹测试学社测开21期项目实战

学院课程由一线大厂测试经理与资深测试开发专家参与研发，以实战驱动为导向，紧贴互联网名企的用人需求。课程方向涵盖移动app自动化测试、接口自动化测试、性能测试、安全测试、持续集成/持续交付/DevOps，测试左移、测试右移、精准测试、测试平台开发、测试管理等内容，全面提升测试开发工程师的技术实力。课程技术涵盖pytest、junit、selenium、appium、postman、requests、httprunner、jmeter、jenkins、docker、k8s、elasticsearch、sonarqube、jacoco、jvm-sandbox等相关技术。

加入测试开发技术交流社群，请扫码：

![测试开发gitee渠道|168x168](https://ceshiren.com/uploads/default/original/3X/7/1/712b212a7830ee56b58fa888de492e3c50d87d05.png)

- https://www.pytest.org

## 参数化与数据驱动的区别

- 参数化： 数据以参数的形式传递到测试用例当中
- 数据驱动：
  - 测试数据的数据驱动：使用测试数据驱动测试执行
  - 配置的数据驱动
  - 测试步骤的数据驱动
  - PO的数据驱动

## fixture的用法与 setup 区别

- 命名灵活，任何命名，不要以 test_开头
- fixture 可以以参数的形式传递到测试用例中
- 想用就用，可以在需要fixture的测试用例的参数里，添加需要的fixture，不需要就不传递
- 一条用例可以使用多个fixture 作为前置条件
- autouse 参数可以使fixture 自动执行
- 作用域（session>module>class>function）
- 在测试用例参数化里的位置，可以随便放，前面后面都可以。
- 如果想要在测试用例中使用fixture的返回数据，就要把fixture 名字传递到测试方法的参数列表中。

## conftest.py

- 命名 一定要叫conftest.py
- 存放公共数据，公共方法，一般fixture 会放在这个文件下，
- 测试用例引用里面的方法时，不需要导入操作
- conftest.py 的作用域 当前目录以及所有的子目录生效



[交流论坛](http://qrcode.testing-studio.com/f?from=gitee&url=https://ceshiren.com)

## 关于测吧（北京）科技有限公司

[测吧（北京）科技有限公司](http://qrcode.testing-studio.com/f?from=gitee&url=https://www.testing-studio.com) 是一家服务于测试领域的高科技公司，为企业提供全方位的自动化测试技术支持、测试平台开发定制、测试效能提升等咨询与科研合作服务。凭借优秀的测试开发技术实力先后为华为、工信部、信通院等知名企业与机构提供测试技术支持服务。我们源于测试行业，也希望以专业的态度打造一所能得到行业普遍认可与尊重的高科技企业。

## 推荐学习路径
![技术图谱——1108|800x1156](https://ceshiren.com/uploads/default/original/3X/8/5/85db0854dd6861b7324ec580ac7aab88753cd2eb.jpeg)