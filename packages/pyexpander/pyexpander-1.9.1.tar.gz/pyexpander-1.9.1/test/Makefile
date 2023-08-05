TOP:=$(shell pwd)/..

PYVER:=$(strip $(PYVER))

ifeq (,$(findstring $(PYVER),2 3))
$(error error variable PYVER must be set to 2 or 3)
endif

export PYVER

# set PYTHON only if it is not yet defined:
ifeq (,$(PYTHON))
        PYTHON:=python$(PYVER)
endif

PYEXPANDER_LIB:=pyexpander

BINDIR:=$(TOP)/python$(PYVER)/bin
LIBDIR:=$(TOP)/python$(PYVER)/$(PYEXPANDER_LIB)

export PYTHONPATH:=$(TOP)/python$(PYVER):$(PYTHONPATH)

ifeq ($(PYVER),2)
EXPANDER_BIN=expander2.py
else
EXPANDER_BIN=expander.py
endif

EXPANDER=$(BINDIR)/$(EXPANDER_BIN)

# The list of tests and their order is taken from file "TESTS":
expander_tests:= $(shell grep -v '\#' TESTS  | xargs)

.PRECIOUS: %.out

# set this only to "yes" in order to create the 
# test[n].ok files. These files are later compared to
# the test[n].out files.
# In order for the tests to really test pyexpander, 
# the variable MUST BE set to "no".
CREATE_TESTS=no

all: pure_module_test external_module_test $(addsuffix .tst, $(expander_tests))

clean:
	rm -f $(addsuffix .out, $(expander_tests))

_clean: clean
	rm -f $(addsuffix .ok, $(expander_tests))

pure_module_test:
	@echo -e "\n-> run doctest of python$(PYVER)/$(PYEXPANDER_LIB)/parser.py" >&2
	$(PYTHON) $(LIBDIR)/parser.py
	@echo -e "\n-> run doctest of python$(PYVER)/$(PYEXPANDER_LIB)/lib.py" >&2
	$(PYTHON) $(LIBDIR)/lib.py

external_module_test:
	@echo -e "\n-> test functions in lib.py with external doctest" >&2
	$(PYTHON) ./pyexpander_test.py

ok: $(addsuffix .ok, $(expander_tests))

%.out: %.in
	@echo -e "\n-> test $*" >&2
	$(EXPANDER) -f $< > $@

external-variable.out: external-variable.in
	@echo -e "\n-> test external-variable" >&2
	$(EXPANDER) -f $< --eval 'x=1' > $@

variable-undefined.out: variable-undefined.in
	@echo -e "\n-> test variable-undefined" >&2
	($(EXPANDER) -f $< || true) 2>&1 | \
	    sed -e 's/.*\//  "/;s/line [0-9]\+/line xxx/;s/$(EXPANDER_BIN)/expander.py/;s/\(raise\) NameError, \(.*\)/\1 e.__class__(\2)/;s/\(str(e),\)\([^ ]\)/\1 \2/' > $@

simple-vars-option.out: simple-vars-option.in
	@echo -e "\n-> test simple-vars-option" >&2
	$(EXPANDER) -s -f $< > $@

include-path.out: include-path.in
	@echo -e "\n-> test include-path" >&2
	mkdir x
	echo "\$$py(a+=1)" > x/test.inc
	$(EXPANDER) -f $< -I x > $@
	rm -rf x

for-functionlist.out: for-functionlist.in
	@echo -e "\n-> test for-functionlist" >&2
	$(EXPANDER) -f $< | sed -e 's/<type/<class/' > $@

stdin.out: stdin.in
	$(EXPANDER) < $< > $@

keyword-conflict.out: keyword-conflict.in
	@echo -e "\n-> test keyword-conflict" >&2
	($(EXPANDER) -f $< || true) 2>&1 | \
	    sed -e 's/.*\//  "/;s/line [0-9]\+/line xxx/;s/$(EXPANDER_BIN)/expander.py/;' > $@

keyword-conflict-simple-vars.out: keyword-conflict-simple-vars.in
	@echo -e "\n-> test keyword-conflict-simple-vars" >&2
	echo "----------- pyexpander without '-s'" > $@
	$(EXPANDER) -f $< >> $@ 2>&1
	echo "----------- pyexpander with '-s'" >> $@
	$(EXPANDER) -s -f $< >> $@ 2>&1

auto-continuation.out: auto-continuation.in
	@echo -e "\n-> test auto-continuation" >&2
	echo "----------- pyexpander without '-a'" > $@
	$(EXPANDER) -f $< >> $@ 
	echo "----------- pyexpander with '-a'" >> $@
	$(EXPANDER) -a -f $< >> $@

macro-indent.out: macro-indent.in
	@echo -e "\n-> test macro-indent" >&2
	$(EXPANDER) -a -i -f $< > $@

safe-mode-expression.out: safe-mode-expression.in
	@echo -e "\n-> test safe-mode-expression" >&2
	$(EXPANDER) -a -i -f $< 2>&1 | grep -v '^ ' > $@

safe-mode-py.out: safe-mode-py.in
	@echo -e "\n-> test safe-mode-py" >&2
	$(EXPANDER) -a -i -f $< 2>&1 | grep -v '^ ' > $@

safe-mode-extend.out: safe-mode-extend.in
	@echo -e "\n-> test safe-mode-extend" >&2
	$(EXPANDER) -a -i -f $< 2>&1 | grep -v '^ ' > $@

safe-mode-extend_expr.out: safe-mode-extend_expr.in
	@echo -e "\n-> test safe-mode-extend_expr" >&2
	$(EXPANDER) -a -i -f $< 2>&1 | grep -v '^ ' > $@

ifeq "$(CREATE_TESTS)" "yes"
%.ok: %.out
	cp $< $@
endif

%.tst: %.in %.out %.ok
	diff $(wordlist 2, 3, $+)

#diff $(wordlist 2, 3, $+) || true

