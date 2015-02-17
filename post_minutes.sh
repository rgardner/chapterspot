#!/usr/bin/env bash
# usage: post_minutes.sh <minutes_url>
message="Here are the minutes from today's chapter: $1"
python chapterspot_message.py "$message"
