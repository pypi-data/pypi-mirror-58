# Scrapy Metas Extension

[![CircleCI](https://circleci.com/gh/Kpler/scrapy-job-parameters-extension.svg?style=svg)](https://circleci.com/gh/Kpler/scrapy-job-parameters-extension)

> Scrapy extension to make env meta information available as spider fields.

Current implementation exposes to the spider a `meta` object with the
following attributes:

- `project_id` - as defined by Scrapinghub
- `spider_id` -
- `job_id` -
- `job_name` - raw job id from Scrapinghub or uuid v4
- `job_time` - excecution time
