# Deployment — quick reference

How the FlexiBowl docs site gets deployed.

## Architecture in one paragraph

Pushes to `main` trigger GitHub Actions. Media (`build/_shared/`, `build/_assets/`, and
each language's `build/V. 1.0/<lang>/_images/` and `_downloads/`) syncs to an **AWS S3**
bucket fronted by **CloudFront**. HTML is baked into a tiny nginx Docker image pushed to
**GHCR** (`ghcr.io/flexibowl/flexibowl-docs:latest`). A webhook notifies the Makai Labs
Dokploy server to pull the new image and restart. Live site:
`flexibowl-docs.flexibowl.com`.

(There's a dormant fourth media path, `build/Offline manual.zip` — see "Special case"
below. It's excluded here because it never actually happens today: the archive is never
committed, so there's nothing for this pipeline to pick up.)

## Everyday workflow

- ARS runs `build_manual.bat`, commits, pushes to `main`.
- Site updates within ~1–2 minutes. Nothing else to do.

## Where things live

| Thing                                  | Location                                                |
| --------------------------------------- | -------------------------------------------------------- |
| Source + HTML output                    | This repo                                                 |
| Build pipeline                          | `.github/workflows/deploy.yml`                            |
| Size guard (blocks big non-LFS files)   | `.github/workflows/size-check.yml`                         |
| CDN URL rewriter                        | `tools/ci/rewrite_cdn_urls.py`                             |
| Docker image                            | `ghcr.io/flexibowl/flexibowl-docs`                          |
| Media & big files                       | AWS S3 bucket `flexivision-docs` (eu-south-1, Milan) — **shared with FlexiVision**, see below |
| CDN in front of S3                      | AWS CloudFront distribution `d1nwml7sk3eafv.cloudfront.net` — **shared with FlexiVision**, see below |
| Runtime                                 | Makai Labs Dokploy server, app `flexibowl-docs`             |
| AWS + deploy credentials                | GitHub → Settings → Secrets: 5 shared AWS secrets at **organisation** level (`FlexiBowl` org), 2 at repo level (`CDN_BASE_URL`, `DOKPLOY_WEBHOOK`) |

### The bucket and CDN are shared with FlexiVision

FlexiBowl does not have its own S3 bucket or CloudFront distribution. It reuses
`FlexiVision_One_Documentation`'s existing stack — same bucket, same distribution, same
IAM user — rather than a second one being provisioned. This works because the two sites
write to disjoint key prefixes:

- FlexiVision's objects sit at the **bucket root**: `_shared/…`, `_assets/…`.
- FlexiBowl's objects sit under the **`flexibowl/` prefix**: `flexibowl/_shared/…`,
  `flexibowl/_assets/…`, `flexibowl/V. 1.0/<lang>/_images/…`, etc.

The prefix is applied in exactly two independent places, which must agree and must
never both apply to the same string:

- **`deploy.yml`** applies it to every S3 destination — all four sync/copy targets
  (`_shared`, `_assets`, the per-language `_images`/`_downloads` loop, and the offline
  archive) write to `s3://$S3_BUCKET/flexibowl/…`.
- **The `CDN_BASE_URL` secret** applies it for URLs the rewriter emits —
  `https://d1nwml7sk3eafv.cloudfront.net/flexibowl`, so a rewritten `<img src>` already
  ends in `/flexibowl/_shared/…` before `tools/ci/rewrite_cdn_urls.py` ever runs; the
  rewriter itself knows nothing about the prefix and must stay that way.

This is also why `aws s3 sync --delete` is safe here: `--delete` only removes objects
*within its own destination prefix*, so FlexiBowl's sync can never delete FlexiVision's
root-level keys, and vice versa. The CloudFront invalidation is scoped to
`/flexibowl/*`, not `/*`, for the same reason — an unscoped invalidation would evict
FlexiVision's cached objects on every FlexiBowl deploy.

**If the other manual's media disappears or 404s, suspect a misconfigured sync in
*either* repo first** — a missing or doubled `flexibowl/` prefix in `deploy.yml`, or a
`CDN_BASE_URL` value that doesn't match, are the most likely causes. See
`DEPLOY_SETUP.md` → "Reuse FlexiVision's existing AWS stack" for the full setup
rationale (gitignored — ask Makai Labs if you need it and don't have it).

## Check deploy status

- **Currently deploying?** Repo → Actions tab. Green = done.
- **Deploy failed?** Click the red run, read the failed step. A common one: `Assert no
  LFS-tracked file can reach the image` failing with `::error file=...::LFS-tracked file
  is not excluded by .dockerignore` — a new binary file type reached the repo without a
  matching `.dockerignore` rule. Add the exclusion (or route the file through the CDN
  offload instead) and push again.
- **Site stale?** Confirm the latest run is green in the Actions tab. If it is but the
  site still shows old content after a few minutes, the Dokploy server didn't pick up
  the new image — ping Makai Labs.
- **Media missing?** Check the S3 bucket's Objects tab under the `flexibowl/` prefix for
  the file — not the bucket root, that's FlexiVision's. If absent, re-run the workflow
  manually from Actions.
- **Old media still showing?** CloudFront cache. Wait for TTL to expire, or trigger an
  invalidation manually (AWS console → CloudFront → distribution → Invalidations →
  `Create invalidation` → path `/flexibowl/*`). **Never use `/*`** — the distribution is
  shared with FlexiVision, and an unscoped invalidation evicts their cached objects too.

## Common actions

### Rollback

1. Quick: revert the bad commit on `main`, push. CI re-deploys.
2. Faster: ask Makai Labs to swap the deployed image tag back to a previous commit SHA.
   Every workflow run pushes both `:latest` and `:<commit-sha>` to
   `ghcr.io/flexibowl/flexibowl-docs`, so any past green commit is still pullable.

### Rotate AWS credentials

This IAM user and access key are **shared with FlexiVision** — the same credentials
authenticate both repos' workflows. AWS IAM → Users → deactivate the old access key,
create a new one → update `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, which are
**organisation-level secrets on the `FlexiBowl` GitHub org**, not secrets on this repo.
Coordinate with whoever owns FlexiVision's deploy before rotating — a mid-rotation gap
breaks both sites' next deploy, not just this one.

### Extend the list of files that go to LFS

Edit `.gitattributes`, add the pattern, commit. New files follow the rule; old files
stay where they are.

### Adding new downloads (PDFs, zips, large images, etc.)

For an asset shared across every version and language, drop the file into
`sources/_shared/media/` (under `images/`, `videos/`, or `documents/`) and link to it
from your Markdown source with a normal relative path. The next `build_manual.bat` run
copies it into `build/_shared/`, and CI takes care of the rest: the file is uploaded to
the CDN — not baked into the docs image — and the link in your HTML is rewritten to
point at the CDN automatically.

For a document that belongs to a single manual/language only (for example a PDF linked
from one page), just link to it normally from the Markdown source — Sphinx collects it
automatically into that language's `_downloads/` folder at build time. See the next
section for how that gets offloaded to the CDN.

The one exception is the offline manual archive itself — that one is a single file for
the whole site, produced by the build rather than linked from Markdown. See "Special
case: `build/Offline manual.zip`" below.

**Don't** hand-edit anything under `build/` directly. It's regenerated by
`build_manual.bat`, so manual additions are lost on the next build.

### Special case: `build/Offline manual.zip` — feature is off, and stays off

`build_manual.bat --mode full` produces `build/Offline manual.zip`, an archive of the
entire built site including media — roughly **1.5 GB** for this manual. (A `quick`
build doesn't produce it, and `quick` is the normal case.)

**It is not committed, and committing it is not viable.** GitHub's free Git LFS tier is
1 GB of storage total, and a single LFS object is capped at 2 GB — this archive alone
would blow through the storage cap on the very first push. There's no config change
that fixes this; it's a hard ceiling for a repo this size.

Consequently the "Download offline manual" button is **not shown** on the live site.
The publisher sets `offlineZipEnabled = false` in every page whenever no archive is
present at build time (`configure_release_download_flags()` in `manual_publisher.py`),
and since the archive is never committed, that's the state of every build today — every
one of this manual's 479 built HTML files carries `offlineZipEnabled = false` right now.
FlexiVision's docs are in the identical state (605 files, same flag, same reason). This
is a deliberate, permanent call for both repos, not something half-finished.

The deployment plumbing for the feature is real and correct, and it's fine that it sits
unused — it costs nothing to leave in place:

- `.dockerignore` excludes `build/Offline manual.zip` from the Docker image.
- `deploy.yml`'s `sync-s3` job uploads it to S3 when present, and logs and skips
  without failing the build when it isn't — which is every push so far.
- `nginx.conf` 302-redirects `/Offline manual.zip` to the CDN copy, for the moment the
  JS-built download button gets clicked.

If you find this machinery and no archive to go with it, that's expected: it's
**dormant, not broken**.

If the offline download is ever actually wanted, the only viable path is to stop
treating the archive as a committed file: produce it in CI (or another artifact store)
and push it straight to S3 without ever putting it in git, and have that same step flip
`offlineZipEnabled = true`. That's a deliberate infrastructure change with its own
design work — not something that turns on by itself, and not a default any of this
plumbing assumes.

If `build_manual.bat` is ever changed to rename or relocate the archive, ping Makai
Labs so the redirect, the `.dockerignore` rule, and the LFS-guard allowlist — all still
live even with the feature off — can be updated together.

### Per-language `_images/` and `_downloads/` offload

Unlike FlexiVision, this manual emits per-language asset directories —
`build/V. 1.0/<lang>/_images/` and `build/V. 1.0/<lang>/_downloads/` — because each
language build embeds figures and Sphinx-collected downloads relative to its own HTML
files rather than to the build root. CI finds every directory named `_images` or
`_downloads` anywhere under `build/` and syncs it to S3 under its build-root-relative
key, prefixed `flexibowl/` (e.g. `build/V. 1.0/IT/_images/...` →
`s3://flexivision-docs/flexibowl/V. 1.0/IT/_images/...` — note the bucket is
`flexivision-docs`, shared with FlexiVision, not a `flexibowl-docs` bucket of its own;
see "The bucket and CDN are shared with FlexiVision" above).
`tools/ci/rewrite_cdn_urls.py` resolves and rewrites the matching `src=`/`href=`
references in the HTML to the CDN URL before the Docker image is built — it has no
knowledge of the `flexibowl/` prefix at all, since that's already baked into
`CDN_BASE_URL` before the rewriter ever runs. This runs automatically on every push,
same as `_shared/` and `_assets/` — you don't need to do anything differently.

### Move to a different CDN URL or bucket

`S3_BUCKET_NAME` and `CLOUDFRONT_DISTRIBUTION_ID` are organisation-level secrets shared
with FlexiVision (see above) — don't change them here without coordinating, since that
would repoint FlexiVision's deploy too. `CDN_BASE_URL` is this repo's own secret; update
it (keeping the `/flexibowl` path, or whatever prefix the new target uses) and the next
push rewrites HTML URLs to the new target and syncs there.

### Force a fresh CDN cache

Manual invalidation in CloudFront, path `/flexibowl/*` — **not** `/*`, which would also
evict FlexiVision's cached objects from the shared distribution. First 1000 invalidation
paths/month are free; `/flexibowl/*` counts as one path.

## Known limits

- Images are capped at 2560 px wide by the build (`tools/manual_publisher/image_cap.py`)
  — anything wider is downscaled automatically, so there's no need to resize hi-res CAD
  exports by hand before committing.
- AWS S3 storage (Milan / eu-south-1): ~$0.0245/GB/month.
- CloudFront egress: ~$0.085/GB out (Europe/US). Expect ~$1–5/month for a typical docs
  site.
- CloudFront invalidations: 1000 paths/month free, then $0.005/path.
- GitHub LFS: free up to 1 GB storage + 1 GB/month bandwidth. Buy a $5/month pack if
  exceeded.
- Single file over 100 MB must be LFS-tracked or GitHub rejects the push.
- Size-check workflow blocks non-LFS files > 10 MB.
- `build/Offline manual.zip` (from a full build) is ~1.5 GB — well past what the 1 GB
  free LFS tier can hold. It is not committed and the download feature stays off for
  that reason. See "Special case" above.
- **The AWS blast radius is shared with FlexiVision**, not per-repo: one IAM key pair,
  one S3 bucket, one CloudFront distribution serve both docs sites. There is no AWS-side
  isolation between them — the `flexibowl/` key prefix (and the matching invalidation
  scope) is the *only* thing separating FlexiBowl's media from FlexiVision's. If either
  site's media suddenly goes missing or starts 404ing, the first thing to suspect is a
  misconfigured sync in the *other* repo — a dropped, doubled, or wrong `flexibowl/`
  prefix in `deploy.yml`, or a `CDN_BASE_URL` secret that no longer matches. Rotating
  the shared AWS credentials also affects both sites; see `DEPLOY_SETUP.md`'s FAQ.

## If everything is on fire

- Ask Makai Labs to pause auto-deploy on the Dokploy server so a broken push doesn't
  keep propagating while you investigate.
- There is no GitHub Pages fallback: the Pages workflows were deleted as part of this
  migration. The fallback is to redeploy a previous image tag from GHCR — pick the last
  known-good commit SHA (every workflow run pushes both `:latest` and
  `:<commit-sha>` to `ghcr.io/flexibowl/flexibowl-docs`) and ask Makai Labs to point the
  Dokploy `flexibowl-docs` app at that tag instead of `:latest`, then redeploy manually.

## Who to contact

- Repo + deploy: Makai Labs
- AWS account / CloudFront: Makai Labs
- ARS edits content only — he should not need to touch this file.
