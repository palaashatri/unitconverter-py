# Test Plan and Output

|   Function    | Based On      | Test Function | Function Used |Input  |  Expected O/P |  Real O/P  |  Status  | 
| ------------- | ------------- | --- |------ | ---  |------------ |  --------- |  ------  |
| Digital          | Requirement   | `test_convert_digital()`  | `convert_digital.convert()` | `1,"kB","byte"`   |    1000      |    1000   |    ✔    |
| Weight        | Requirement   | `test_convert_weight()` |  `convert_weight.convert()` | `1,"kg","g"`  |     1000        |      1000     |     ✔    |
| Length        | Requirement   | `test_convert_length()`  | `convert_length.convert()` | `1000,"cm","m"`   |     10      |      10   |    ✔    |
| Area       | Requirement   | `test_convert_area()`   | `convert_area.convert()` | `1,"sqm","sqcm"`   |    10000    |    10000  |    ✔    |
| Temperature      | Requirement   | `test_convert_temp()`   | `convert_temp.convert_celTokel()` | `38`   |    311.5    |    311.5  |    ✔    |
| Temperature      | Requirement   | `test_convert_temp()`   | `convert_temp.convert_celTofah()` | `38`   |    100.4    |    100.4  |    ✔    |
