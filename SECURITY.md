# Security Policy

## Reporting a Vulnerability

**DO NOT CREATE PUBLIC ISSUES FOR SECURITY VULNERABILITIES**

If you discover any security-related issues, please report them privately:

1. **Email security advisories to**:  
   `gelir6714@gmail.com` (not monitored by bots)  

2. **Use GitHub Private Vulnerability Reporting** (preferred):  
   [Report vulnerability](https://github.com/mystic-poop/Disware/security/advisories/new)

### What to include in your report
- Project version and environment details
- Steps to reproduce the vulnerability
- Impact analysis and potential attack scenarios
- Any mitigation suggestions
- Your disclosure preferences

## Our Response Process

1. **Acknowledgement**:  
   You'll receive confirmation of your report within 3 business days
2. **Investigation**:  
   Initial assessment within 7 days
3. **Fix Development**:  
   Patch development with regular updates
4. **Release**:  
   Coordinated release with [CVE assignment](https://cve.mitre.org/)
5. **Public Disclosure**:  
   After patch availability (typically 30-90 days post-fix)

## Vulnerability Management

### In-Scope Vulnerabilities
- Remote code execution (RCE)
- Authentication bypasses
- Privilege escalation
- Sensitive data exposure
- Critical dependency vulnerabilities
- Supply chain compromises

### Out-of-Scope
- Theoretical vulnerabilities without PoC
- Self-XSS or low-impact CSRF
- Missing security headers without demonstrated impact
- Denial of Service (DoS) vulnerabilities
- Vulnerabilities in dependencies without known exploits

## Security Updates
Security patches are released as:
- Immediate patch releases
- Security bulletins in [GitHub Releases](https://github.com/mystic-poop/Disware/releases)
- [GitHub Security Advisories](https://github.com/mystic-poop/Disware/security/advisories)

## Security Best Practices for Users
1. Always run Disware in a sandboxed environment
2. Regularly update to the latest stable version
