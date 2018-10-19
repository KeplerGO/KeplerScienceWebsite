PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output

CONFFILE=$(BASEDIR)/pelicanconf.py
DEVCONF=$(BASEDIR)/pelicanconf-dev.py
LIVECONF=$(BASEDIR)/pelicanconf-live.py

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
	@echo '   make quick                       generate locally with caching (news listing will be empty)'
	@echo '   make html                        generate locally                   '
	@echo '   make html-dev                    generate for github.io dev server  '
	@echo '   make html-live                   generate for production web server '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make upload                      upload the web site via rsync+ssh  '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '   make kpub                        update the publication stats (requires kpub)'
	@echo '                                                                       '
	@echo 'Set DEBUG to 1 to enable Pelican debugging, e.g. make DEBUG=1 html     '
	@echo '                                                                       '

quick:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

html-dev:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(DEVCONF) $(PELICANOPTS) --ignore-cache

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) --ignore-cache

html-live: clean
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(LIVECONF) $(PELICANOPTS) --ignore-cache

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

upload: html-live
	@if [ $(shell git status -s | wc -l) -gt 0 ]; then \
	  	echo "***WARNING***"; \
	  	echo "You have uncommitted changes in this repository (run 'git status' for details)."; \
	  	echo "Please add/commit/push these changes to GitHub before uploading to the webserver.\n"; \
	  	echo "Press Ctrl-C to go back, or any other key to continue the upload."; \
	  read $foo; \
	fi
	rsync -rvPzc --cvs-exclude -e "ssh -I $(OPENSC_DIR)" $(OUTPUTDIR)/ $(KEPLERWEB_USER)@$(KEPLERWEB_HOST):$(KEPLERWEB_DIR)

github: html-dev
	ghp-import -m "Generate dev site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

#Make live is deprecated, use make upload instead
#live:
	#ghp-import -m "Generate live site" -b $(GITHUB_LIVE_BRANCH) $(OUTPUTDIR)
	#git push origin $(GITHUB_LIVE_BRANCH)

kpub:
	cd content/pages/kpub; \
	kpub --save
	cd content/images/kpub; \
	kpub-plot
	cd content/data; \
	kpub-spreadsheet
	git add content/pages/kpub/* content/images/kpub/* content/data/kepler-publications.xls
	git commit -m "Publication stats update"

.PHONY: html html-dev html-live help clean regenerate serve devserver ssh_upload rsync_upload github live kpub
