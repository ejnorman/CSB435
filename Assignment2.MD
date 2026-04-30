# FroggyHealthPortal Security Audit
**Consultant:**
**Date:**

---

## Part 1: Injection Vulnerability Analysis (50 points)

### Code Snippet 1: Patient Search (10 points)

**1. What type of injection vulnerability exists here?**

> _Your answer here._

**2. Example attack payload:**

```
Your payload here
```

**3. What damage could an attacker do with this vulnerability?**

> _Your answer here._

---

### Code Snippet 2: Medical Report Generator (10 points)

**1. What type of injection vulnerability exists here?**

> _Your answer here._

**2. Example attack payload:**

```
Your payload here
```

**3. What could an attacker do with this vulnerability?**

> _Your answer here._

**4. Why are shell commands with user input dangerous?**

> _Your answer here._

---

### Code Snippet 3: Patient Notes Display (10 points)

**Vulnerability 1:**

- **Type of injection:**

  > _Your answer here._

- **Attack payload:**

  ```
  Your payload here
  ```

- **Impact:**

  > _Your answer here._

**Vulnerability 2:**

- **Type of injection:**

  > _Your answer here._

- **Attack payload:**

  ```
  Your payload here
  ```

- **Impact:**

  > _Your answer here._

---

### Code Snippet 4: Prescription Lookup (10 points)

**1. Identify both SQL injection vulnerabilities:**

> _Your answer here._

**2. `patient_id` parameter:**

- **Why is it vulnerable even without quotes?**

  > _Your answer here._

- **Attack payload:**

  ```
  Your payload here
  ```

**3. `medication` parameter:**

- **UNION injection to dump all patient data:**

  ```
  Your payload here
  ```

- **How does this attack work?**

  > _Your answer here._

---

### Code Snippet 5: Appointment Email Notifications (10 points)

**1. What injection vulnerability exists here?**

> _Your answer here._

**2. Attack payload that executes arbitrary commands:**

```
Your payload here
```

**3. Step-by-step explanation of how the attack works:**

> _Your answer here._

**4. When should `shell=True` be used in Python subprocess?**

> _Your answer here._

---

## Part 2: Cryptography Mistakes (30 points)

### Code Snippet 6: Password Storage (15 points)

**Cryptography Mistake 1:**

- **What's wrong?**

  > _Your answer here._

- **What attack does this enable?**

  > _Your answer here._

- **How would you fix it?**

  > _Your answer here._

**Cryptography Mistake 2:**

- **What's wrong?**

  > _Your answer here._

- **What attack does this enable?**

  > _Your answer here._

- **How would you fix it?**

  > _Your answer here._

**Does `check_password` have an exploitable timing attack vulnerability?**

> _Your answer here._

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
