# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The TensorBoard Debugger V2 plugin."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from werkzeug import wrappers

from tensorboard import plugin_util
from tensorboard.plugins import base_plugin
from tensorboard.plugins.debugger_v2 import debug_data_provider
from tensorboard.backend import http_util


class DebuggerV2Plugin(base_plugin.TBPlugin):
    """Debugger V2 Plugin for TensorBoard."""

    plugin_name = "debugger-v2"

    def __init__(self, context):
        """Instantiates Debugger V2 Plugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
        super(DebuggerV2Plugin, self).__init__(context)
        self._logdir = context.logdir
        # TODO(cais): Implement factory for DataProvider that takes into account
        # the settings.
        self._data_provider = debug_data_provider.LocalDebuggerV2DataProvider(
            self._logdir
        )

    def get_plugin_apps(self):
        # TODO(cais): Add routes as they are implemented.
        return {
            "/runs": self.serve_runs,
        }

    def is_active(self):
        """Check whether the Debugger V2 Plugin is always active.

        When no data in the tfdbg v2 format is available, a custom information
        screen is displayed to instruct the user on how to generate such data
        to be able to use the plugin.

        Returns:
          `True` if and only if data in tfdbg v2's DebugEvent format is available.
        """
        # TODO(cais): Implement logic.
        return False

    def frontend_metadata(self):
        return base_plugin.FrontendMetadata(
            is_ng_component=True, tab_name="Debugger V2", disable_reload=True
        )

    @wrappers.Request.application
    def serve_runs(self, request):
        experiment = plugin_util.experiment_id(request.environ)
        runs = self._data_provider.list_runs(experiment)
        return http_util.Respond(
            request, [run.run_id for run in runs], "application/json"
        )
