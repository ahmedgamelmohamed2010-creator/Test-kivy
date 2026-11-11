# Kivy APK Test

A tiny Kivy app for testing Android APK builds with GitHub Actions.

## Project files

- `main.py` - the Kivy test application.
- `buildozer.spec` - Buildozer configuration.
- `.github/workflows/build.yml` - GitHub Actions workflow.

## Build on GitHub using a tablet or phone

1. Create a GitHub repository.
2. Upload all files and folders from this project. Keep the workflow path exactly:
   `.github/workflows/build.yml`
3. Make sure the default branch is named `main`.
4. Open the repository's **Actions** tab.
5. Select **Build Kivy Android APK**.
6. Press **Run workflow** (or push/commit to `main` to trigger it).
7. Open the completed workflow run.
8. Under **Artifacts**, download `Kivy-APK-Test`.
9. Extract the ZIP file and install the APK on your Android device.

## Expected test

The app should open with the title "Kivy APK Test", a message, and a
"Tap me" button. Each tap should increase the click counter.

## Notes

- The APK is built on a GitHub-hosted Ubuntu runner, not on the tablet.
- This workflow produces a debug APK for testing, not a signed Play Store release.
- The build can take several minutes on the first run.
- If the build fails, open the workflow run and inspect the first failing step
  and its log. Share that error log for troubleshooting.
- This project targets `arm64-v8a`, suitable for most modern 64-bit Android
  devices. Device compatibility still depends on the Android version and
  hardware.
