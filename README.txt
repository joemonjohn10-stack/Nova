NOVA — PORTABLE OFFLINE-FIRST RELEASE CANDIDATE
================================================

WHAT THIS BUILD DOES
- One responsive web app layout for phone and Windows screens.
- Installable PWA shell when served from HTTPS (or localhost) by a compatible browser.
- Offline app shell caching after the first successful online load/install.
- Local conversations, history, approved memories, projects, tasks and notes.
- Offline workspace commands: help, add task, add note, save memory, search local data, basic arithmetic, device date/time and focus timer.
- Browser speech input/output where supported. Speech recognition may rely on an online browser service; it is not guaranteed offline.
- Export a portable JSON backup and restore it on another device. Backups deliberately exclude AI credentials.
- Optional save-file picker on supporting browsers; otherwise the backup downloads and can be moved to the USB drive using the device's file manager.
- OpenAI-compatible Chat Completions provider connection and test control.
- API key is kept in session storage for the current browser session, not in the persistent NOVA backup/local workspace.

IMPORTANT: HOW TO USE THE USB
The USB stores the NOVA package and portable backups. It does not itself run the app or provide the phone's processing power.
1. Keep the extracted NOVA folder on the USB as your master copy. On Android, use the Files app to open the NOVA folder and try opening index.html with Chrome. If Chrome refuses the page or local storage, use an HTTPS-hosted copy instead; the USB file alone cannot enable PWA installation/service workers. On Windows, use START_NOVA.bat.
2. For backup: in NOVA > Settings > Data & privacy, choose Download USB backup. If a save picker appears, select the USB. Otherwise move the downloaded JSON file to the USB in the Files app.
3. On the other device, open NOVA and choose Restore from USB, then select that JSON file.
4. Restore replaces the current workspace on that device. Export a backup first if you need to preserve its data.

ANDROID + WINDOWS: CURRENT REALITY
This is one responsive web app, not a native Android APK and not a Windows installer. To get the reliable installable/offline PWA experience on both devices, the app must be served from an HTTPS website at least once on each device. After the first successful load, its app shell can open offline. Directly opening index.html from a USB drive may work only as a basic preview; browser security rules can block storage, service workers, installation and other features for file:// pages. Therefore this ZIP alone does not guarantee a fully installed offline Android app.

AI AND OFFLINE LIMITS
- Offline mode is a local utility/workspace assistant, not a full language model. It can manage and search saved NOVA data and perform the documented basic commands, but it cannot provide general advanced reasoning.
- A true local AI model is not bundled. It must be selected and tested against the phone's RAM, storage, processor and Android compatibility before inclusion. No model performance is claimed.
- Online AI requires an authorised provider endpoint, model and key. No credentials, subscription or inference quota are included.
- The current Python proxy is a Windows/localhost helper. It is not a shared Android backend and does not enable cross-device AI by itself. Android online AI needs a properly secured HTTPS backend or a provider endpoint that explicitly supports browser access. Never expose a secret API key in a public website's frontend.
- Web research, image understanding, cloud sync/accounts, native Android device controls, wake-word listening and background autonomous actions are not implemented in this release.
- Voice input depends on browser support and may use an online recognition service. Do not assume it works without internet.

WINDOWS LOCAL PREVIEW
1. Extract the ZIP.
2. If Python is installed and allowed, run START_NOVA.bat.
3. Keep the terminal window open while using the local server.
4. The local AI proxy binds to 127.0.0.1 only. It is not exposed to other devices.

PRIVACY
- Workspace data is stored locally in the browser on each device and does not automatically sync.
- Exported backups exclude provider credentials.
- The configured AI provider receives the prompts and context sent to it. Review that provider's privacy and retention terms.
- Do not enter provider keys on shared/public/school computers. Remove credentials after use.

TEST STATUS
JavaScript syntax, service-worker syntax, Python syntax, ZIP integrity, and local HTTP delivery of the app shell/assets/API status endpoint have been checked. A real browser automation run was unavailable because no Playwright browser binary was installed. This package is a release candidate, not a fully device-verified final product. A real provider round-trip, Android installation, offline first-load/second-load test, USB picker test and testing on the user's actual devices still require those devices and services. No such device/provider test is claimed here.
