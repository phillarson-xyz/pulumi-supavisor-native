PROJECT_NAME := Pulumi SupavisorNative Resource Provider

SHELL = /bin/bash

PACK             := supavisor-native
PACKDIR          := sdk
PROJECT          := /Users/plarson/Source/phillarson-xyz/pulumi-supavisor-native
NODE_MODULE_NAME := @phillarson-xyz/pulumi-supavisor-native
NUGET_PKG_NAME   := Pulumi.SupavisorNative

PROVIDER        := pulumi-resource-${PACK}
CODEGEN         := pulumi-gen-${PACK}
VERSION         ?= $(shell pulumictl get version)
PROVIDER_PATH   := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

SCHEMA_FILE     := provider/cmd/pulumi-resource-supavisor-native/schema.json
GOPATH			:= $(shell go env GOPATH)

WORKING_DIR     := $(shell pwd)
TESTPARALLELISM := 4

ensure::
	cd provider && GO111MODULE=on go mod tidy
	cd sdk && GO111MODULE=on go mod tidy

gen::
	(cd provider && go build -o $(WORKING_DIR)/bin/${CODEGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/$(CODEGEN))

generate_schema::
	echo "Generating Pulumi schema..."
	$(WORKING_DIR)/bin/$(CODEGEN) -v=3 --logtostderr schema $(SCHEMA_FILE) $(CURDIR)
	echo "Finished generating schema."

provider::
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

provider_debug::
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -gcflags="all=-N -l" -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

test_provider::
	cd provider/pkg && go test -short -v -count=1 -cover -timeout 2h -parallel ${TESTPARALLELISM} ./...

dotnet_sdk:: DOTNET_VERSION := $(shell pulumictl get version --language dotnet)
dotnet_sdk::
	rm -rf sdk/dotnet
	$(WORKING_DIR)/bin/$(CODEGEN) -version=${DOTNET_VERSION} dotnet $(SCHEMA_FILE) $(CURDIR)
	cd ${PACKDIR}/dotnet/&& \
		echo "${DOTNET_VERSION}" >version.txt && \
		dotnet build /p:Version=${DOTNET_VERSION}

go_sdk::
	rm -rf sdk/go
	$(WORKING_DIR)/bin/$(CODEGEN) -version=${VERSION} go $(SCHEMA_FILE) $(CURDIR)

nodejs_sdk:: VERSION := $(shell pulumictl get version --language javascript)
nodejs_sdk::
	rm -rf sdk/nodejs
	$(WORKING_DIR)/bin/$(CODEGEN) -version=${VERSION} nodejs $(SCHEMA_FILE) $(CURDIR)
	cd ${PACKDIR}/nodejs/ && \
		yarn install && \
		yarn run tsc && \
		cp ../../README.md ../../LICENSE package.json yarn.lock bin/ && \
		sed -i.bak 's/$${VERSION}/$(VERSION)/g' bin/package.json

python_sdk:: PYPI_VERSION := $(shell pulumictl get version --language python)
python_sdk::
	rm -rf sdk/python
	$(WORKING_DIR)/bin/$(CODEGEN) -version=${VERSION} python $(SCHEMA_FILE) $(CURDIR)

	cp README.md ${PACKDIR}/python/
	cd ${PACKDIR}/python/ && \
		rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
		sed -i.bak -e 's/^  version = .*/  version = "$(PYPI_VERSION)"/g' ./bin/pyproject.toml && \
        rm ./bin/pyproject.toml.bak && \
		python3 -m venv venv && \
		./venv/bin/python -m pip install build && \
		cd ./bin && \
		../venv/bin/python -m build .

.PHONY: build
build:: gen generate_schema provider dotnet_sdk go_sdk nodejs_sdk python_sdk

# Required for the codegen action that runs in pulumi/pulumi
only_build:: build

lint::
	for DIR in "provider" "sdk" ; do \
		pushd $$DIR && golangci-lint run -c ../.golangci.yml --timeout 10m && popd ; \
	done


install:: install_nodejs_sdk install_dotnet_sdk
	cp $(WORKING_DIR)/bin/${PROVIDER} ${GOPATH}/bin


GO_TEST 	 := go test -v -count=1 -cover -timeout 2h -parallel ${TESTPARALLELISM}

test::
	cd provider/pkg && $(GO_TEST) ./...

test_all::
	cd provider/pkg && $(GO_TEST) ./...
	cd tests/sdk/nodejs && $(GO_TEST) ./...
	cd tests/sdk/python && $(GO_TEST) ./...
	cd tests/sdk/dotnet && $(GO_TEST) ./...
	cd tests/sdk/go && $(GO_TEST) ./...

install_dotnet_sdk::
	rm -rf $(WORKING_DIR)/nuget/$(NUGET_PKG_NAME).*.nupkg
	mkdir -p $(WORKING_DIR)/nuget
	find . -name '*.nupkg' -print -exec cp -p {} ${WORKING_DIR}/nuget \;

install_python_sdk::
	#target intentionally blank

install_go_sdk::
	#target intentionally blank

install_nodejs_sdk::
	-yarn unlink --cwd $(WORKING_DIR)/sdk/nodejs/bin
	yarn link --cwd $(WORKING_DIR)/sdk/nodejs/bin
