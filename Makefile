PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output

CONFFILE=$(BASEDIR)/pelicanconf.py
DEVCONF=$(BASEDIR)/pelicanconf-dev.py
LIVECONF=$(BASEDIR)/pelicanconf-live.py

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

GITHUB_PAGES_BRANCH=gh-pages
GITHUB_LIVE_BRANCH=live

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        generate for local use             '
	@echo '   make html-dev                    generate for github.io dev server  '
	@echo '   make html-live                   generate for production web server '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '   make kpub                        update the publication stats (requires kpub)'
	@echo '                                                                       '
	@echo 'Set DEBUG to 1 to enable Pelican debugging, e.g. make DEBUG=1 html     '
	@echo '                                                                       '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

html-dev:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(DEVCONF) $(PELICANOPTS)

html-live:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(LIVECONF) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

ssh_upload: html-live
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: html-live
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

github: html-dev
	ghp-import -m "Generate dev site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

live: html-live
	ghp-import -m "Generate live site" -b $(GITHUB_LIVE_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_LIVE_BRANCH)

kpub:
	cd content/pages/kpub; \
	kpub --save
	cd content/images/kpub; \
	kpub-plot
	git add content/pages/kpub/* content/images/kpub/*
	git commit -m "Publication stats update"

.PHONY: html html-dev html-live help clean regenerate serve devserver ssh_upload rsync_upload github live kpub
