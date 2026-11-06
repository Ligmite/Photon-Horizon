@echo off
rem Builds Photon-Horizon.zip from the pack sources, bypassing the PowerShell
rem execution policy for this one invocation.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-pack.ps1" %*
