#!/usr/bin/env python3

import sys
import csv
import frontmatter

fieldnames = ["dataset", "field", "guidance", "hint"]

w = csv.DictWriter(open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction='ignore')
w.writeheader()

for row in csv.DictReader(open("specification/dataset.csv", newline="")):
    dataset = row["schema"] = row["dataset"]
    path = "content/dataset/%s.md" % dataset

    post = frontmatter.load(path)
    for field in post.metadata["fields"]:
        w.writerow({"dataset": dataset, "field": field["field"], "guidance": field.get("guidance", "")})
