# AtWtLib
## 1.Main Feature
### 1.`atwt()`
**Usage:**`atwt(int)`  
**Function:** Returns the atomic weight of the element  
**Return: Float** or **Int**.  
**Example:**
```
>>> print(atwt(54))
131.293
```
**Note:** The calculation range is **1 to 127**,
Data of element is from **IUPAC 2013** standards.  

### 2.`mcwt()`
**Usage:**`mcwt(string)`  
**Function:** Returns the atomic weight of the molecular.  
**Return: Float** or **Int**.  
**Example:**
```
>>> print(mcwt("Li2CO3"))
73.89
```
**Note:** The calculation range is **H** to **Og**,
Data of element is from **IUPAC 2013** standards.  
This function can't calculate **Ion, Complex** and
material with **multiple** bracelets.

## 2.Additional Feature
### 1.`info_atwt()`
**Argument:**`info_atwt(bool)`
### 2.`rad()`
=`math.radius()`
### 3.`deg()`
=`math.degree()`
### 4.`eng()`
**Argument:** `num`
### 5.`qbrt()`
**Argument:** `num`
### 6.`root()`
**Argument:**`times,num`
### 7.`lcm()`
**Argument:**`num1,num2`
### 8.`swap()`
**Argument:**`list,num1,num2`
