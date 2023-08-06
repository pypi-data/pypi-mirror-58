# coding=utf-8

#
# Wi-Fi simple geolocation library
# Copyright (c) 2015 - 2019 EasyCoding Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


class Messages:
    arg_desc_yandex: str = 'Use Yandex Geolocation API.'
    arg_desc_google: str = 'Use Google Geolocation API.'
    arg_desc_mozilla: str = 'Use Mozilla Geolocation API.'
    backend_result: str = '%s results:\nLatitude: %.6f\nLongitude: %.6f\n'
    backend_error: str = 'An error occurred while querying %s backend.'
