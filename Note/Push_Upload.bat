@echo off
cd /d D:\ai_exam

set commit_msg=Update %DATE% %TIME%
git add .
git commit -m "%DATE% %TIME%"
git push

pause