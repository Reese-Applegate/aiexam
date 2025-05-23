#!/bin/bash

# 디렉토리 이동 (필요 시 경로 수정)
cd /c/ai_exam || exit 1

# Git LFS 초기화 (한 번만 실행되면 됨)
git lfs install

# 10MB 이상 파일 모두 LFS로 추적 (단 .git 폴더 제외)
find . -type f -size +10M ! -path "./.git/*" -exec git lfs track "{}" \;

# .gitattributes 변경 사항 커밋에 포함
git add .gitattributes

# 모든 변경 사항 스테이징
git add .

# 현재 날짜와 시간으로 커밋 메시지 생성
commit_msg="Auto push: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_msg"

# 원격 저장소로 푸시
git push

# 완료 메시지
echo "✅ Git push completed."
read -p "Press Enter to exit..."