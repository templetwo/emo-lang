# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x (alpha) | :white_check_mark: |

**Note:** Emo-Lang is in alpha status. Use in production environments is not recommended.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please email: **security@thetempleoftwo.com**

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if known)

### What to expect

1. **Acknowledgment:** Response within 48 hours
2. **Investigation:** We will assess severity and impact
3. **Resolution:** Security patch release with credit to reporter (unless anonymous preferred)

## Security Considerations

### Arbitrary Code Execution
- Emo-Lang executes .emo programs as Python code
- **Never run untrusted .emo files** — they could contain malicious code
- Review all .emo programs before execution
- Consider running in sandboxed environments (Docker, VMs) when testing untrusted code

### Glyph Parsing
- Malicious Unicode sequences could potentially crash the parser
- If you encounter parsing issues with untrusted input, please report them

### Emotion Transmuter
- The emotion-to-code transmuter generates executable code from text input
- Review generated code before execution
- Do not use with untrusted user input in production

### Dependencies
- Keep dependencies updated: `pip install --upgrade -r requirements.txt`
- Emo-Lang is experimental — expect security issues in alpha

## Best Practices

1. **Sandbox execution:** Run .emo programs in isolated environments
2. **Code review:** Always review .emo code before execution
3. **Input validation:** Sanitize inputs if accepting .emo programs from users
4. **Regular updates:** Keep Emo-Lang and dependencies up to date

## Responsible Disclosure

We appreciate security researchers. Please:
- Give us reasonable time to fix vulnerabilities before public disclosure
- We will work with you on coordinated disclosure
- We will credit you in release notes (if desired)

Thank you for helping improve Emo-Lang security!
