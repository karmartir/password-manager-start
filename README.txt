==================================================
              SECURE PASSWORD MANAGER
==================================================

Developed by: Garen (Karen Martirosyan)(v2.0)

A feature-rich desktop password manager built with Python and Tkinter.
While initially inspired by foundational concepts from Angela Yu's
Python curriculum, this application has been independently architected,
redesigned, and substantially extended with professional-grade UI/UX
state management and robust security protections.


--- CUSTOM ENGINEERING & ADVANCED FEATURES ---

1. STATE-MACHINE UI & DYNAMIC BUTTON MORPHING
   - Unlike basic tutorials, this app features a true state-driven interface.
   - The "Search" button dynamically morphs into a "Reset" button upon a
     successful record lookup, and transforms back once cleared.

2. HIGH-CONTRAST "NEGATIVE" SECURITY MODE
   - When viewing historical/retrieved credentials, all input fields
     automatically invert to a secure terminal style (white text on a
     deep black background) to visually flag locked data.

3. PREVENTATIVE STATE LOCKS
   - The "Generate Password" button is automatically locked during search
     lookups to completely eliminate the risk of accidentally overwriting
     existing records.

4. 30-SECOND CLIPBOARD AUTO-WIPE
   - Any password generated or retrieved is automatically copied to the clipboard
     and scrubbed clean after exactly 30 seconds to prevent sensitive data
     from lingering in system memory.

5. ROBUST DRY ARCHITECTURE & INPUT VALIDATION
   - Implements clean, reusable file I/O helper functions (`load_data()`,
     `json_dump()`) and strict multi-layer input validation to safeguard
     against empty fields, overflow errors, and malformed data.


--- STANDARD FEATURES ---

- SECURE LOCAL STORAGE: Safely saves credentials in a local 'data.json'
  file created automatically in the app directory.
- BUILT-IN PASSWORD GENERATOR: Instantly creates strong, randomized
  passwords combining letters, numbers, and symbols.


--- HOW TO USE ---

* ADDING A PASSWORD:
  1. Enter the Website and your Email/Username.
  2. Type a password or click "Generate Password".
  3. Click "Add" and confirm your entry to save it.

* FINDING A PASSWORD:
  1. Type the website name into the top field.
  2. Click "Search".
  3. Your credentials will populate, the fields will invert to black,
     and the password will copy to your clipboard for 30 seconds.
  4. Click "Reset" when finished viewing to restore normal mode.