# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from random_flavorpack.api.urls import urlpatterns
from quartet_capture.urls import urlpatterns as capture_patterns
from serialbox.api.urls import urlpatterns as sb_patterns

urlpatterns = urlpatterns + capture_patterns + sb_patterns
