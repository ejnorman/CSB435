# Lab Submission

---

## Dumb Password Rules

### Sites Tested

**Bank of America**
- Already on the list
- No update needed — still enforces the same unusual special character restriction (disallows `!`, `$`, `^`)

**Epic Games**
- Already on the list
- No update needed — still requires passwords longer than 6 characters and disallows spaces; could not confirm the "cannot reuse last 5 passwords" rule

**GovernmentJobs**
- Not on the list
- Should probably be added — requires a minimum of 12 characters, plus uppercase, lowercase, numbers, and symbols; also bans "commonly used words or phrases" with no explanation of what qualifies, making it impossible to know in advance if a password will be accepted

**Yahoo**
- Not on the list
- Does not appear to belong on the list — requires at least 8 characters and includes a real-time password strength meter that prompts users to add characters if the password is too weak; this is reasonable UX, not a dumb rule

---

## Cookie Analysis

### Site Analyzed

**X (Twitter) — x.com**, comparing cookies before and after login

### Cookie Table

| Name | Presence | Domain | Path | Expires | Size | HttpOnly | Secure | SameSite | Purpose |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| __cf_bm | both | .x.com | / | 2026-05-22 | 206 | Yes | Yes | None | Cloudflare bot management |
| __cuid | both | .x.com | / | 2027-06-26 | 42 | No | No | — | User identification |
| _cuid | both | .x.com | / | 2027-06-26 | 42 | No | No | — | User identification (duplicate?) |
| _Secure-STRP | before-login only | .google.com | / | 2026-05-22 | 113 | No | Yes | Strict | Google secure token |
| AEC | before-login only | .google.com | / | 2026-11-18 | 61 | Yes | Yes | Lax | Google anti-CSRF / session |
| att | after-login only | .x.com | / | 2026-05-23 | 45 | Yes | Yes | None | Auth token indicator |
| auth_token | after-login only | .x.com | / | 2027-06-26 | 50 | Yes | Yes | None | Authentication token |
| ct0 | after-login only | .x.com | / | 2027-06-26 | 163 | No | Yes | Lax | CSRF token |
| external_referer | both | .x.com | / | 2026-05-29 | 65 | No | No | — | Referrer tracking |
| g_state | both | .x.com | / | 2026-11-18 | 146 / 94 | No | No | — | Google sign-in state |
| gt | both | .x.com | / | 2026-05-22 | 21 | No | Yes | — | Guest token |
| guest_id | both | .x.com | / | 2027-06-22 | 31 | No | Yes | None | Guest user identifier |
| guest_id_ads | both | .x.com | / | 2027-06-26 | 35 | No | Yes | None | Guest ads targeting |
| guest_id_marketing | both | .x.com | / | 2027-06-26 | 41 | No | Yes | None | Guest marketing tracking |
| kdt | after-login only | .x.com | / | 2027-06-26 | 43 | Yes | Yes | — | Key device token |
| lang | after-login only | .x.com | / | Session | 6 | No | No | — | Language preference |
| NID | before-login only | .google.com | / | 2026-11-21 | 279 | Yes | Yes | None | Google user preference/tracking |
| personalization_id | both | .x.com | / | 2027-06-26 | 47 | No | Yes | None | Personalization/tracking |
| twid | after-login only | .x.com | / | 2027-05-22 | 27 | No | Yes | None | Twitter/X user ID |

### Observations

**Which cookies appear to be for authentication/session management?**

`auth_token`, `ct0`, `att`, `kdt`, `twid`, `gt` 

**Are the authentication cookies properly secured (HttpOnly, Secure, SameSite)?**

`auth_token`, `att`, and `kdt` are all HttpOnly and Secure. `ct0` is not HttpOnly (intentional). `twid` and`gt` are Secure but not HttpOnly.

**Are there any cookies that seem unnecessary or overly permissive?**

- `__cuid` and `_cuid` look to be the same, seems redundant.
- `guest_id`, `guest_id_ads`, and `guest_id_marketing` together could be one cookie.

**Do any cookies have concerning lifetimes (too long or too short)?**

- `auth_token` expires after 1 year, bigger risk of being stolen.
- `guest_id_*` tracks unauthenticated users for 1 year, which is a bit much
- nothing seems too short.
