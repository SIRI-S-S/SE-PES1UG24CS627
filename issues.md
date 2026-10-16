\# Lab 5: Static Code Analysis



Name:Siri S S  

SRN: PES1UG24CS627  

Project:Wildlife Sightings



\## Issues Identified and Fixed



|       **No.**|     **TOOL** |   **Issue                  <br /> Identified**|    **Explanation**|  **Fix Applied** |
|-|-|-|-|-|
|        1|    Bandit|<br />Possible SQL Injection|The SQL query was created using string formatting, which could allow unsafe input to affect the query.|Replaced string formatting with parameterized SQL queries using ? placeholders.|
|        2|    Bandit|Weak MD5 Hash|MD5 is considered weak for security-sensitive hashing.|Replaced MD5 with SHA-256 to generate the observer identifier.|
|        3|    Bandit|<br /><br />Use of assert|Assertions can be removed when Python runs in optimized mode, so they should not be used for essential runtime checks.|Replaced assert with an explicit if condition and RuntimeError.|
|        4|<br /><br />    Pylint|Mutable Default Argument|Using {} as a default argument can cause the same dictionary to be shared between function calls.|Changed the default to None and initialized a new dictionary inside the function.|
|        5|<br /><br />    Pylint|Missing Docstrings|The module and functions did not explain their purpose.|Added module and function docstrings.|
|        6|<br />    Pylint|Incorrect Naming Style|Function names used camelCase instead of the recommended Python snake\_case style.|Renamed functions, such as logSighting to log\_sighting and observerId to observer\_id.|
|        7|  Pylint / Flake8|Long Lines and Formatting Issues|Some lines exceeded the recommended length, and the code contained spacing and naming-style violations.|Split long statements across multiple lines and corrected spacing and variable names.|
|        8|<br />     Pylint|Unnecessary else After return|The else block was unnecessary because the if branch already returned a value.|Removed else and returned the value directly.|
|        9|<br />     Pylint|Missing Empty-Result Handling|The rarest() function could fail if the database contained no sightings.|<br />Added a check that returns "Unknown" when no records are available.|





&#x09;			



Verification Results 



|         **Tool**|    **Before Fixes** |    **After Fixes** |     **Result** |
|-|-|-|-|
|Pylint|3.46/10|10.00/10|Target above 9.5 achieved|
|Bandit|<br />1 high, 1 medium, 1 low severity finding|No issues identified|Findings addressed|
|Flake8|<br />6 reported violations|No reported violations|Formatting checks passed|







Conclusion:

&#x20;         Static code analysis helped identify security risks, code-quality problems, and formatting violations. After applying fixes, the program achieved a Pylint score of 10/10, with no issues reported by Bandit or Flake8.



























































