#!/usr/bin/env python3
# thoth-python
# Copyright(C) 2018, 2019 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""Helper functions and utilities."""

from itertools import chain

from .project import Project


def fill_package_digests(generated_project: Project) -> Project:
    """Temporary fill package digests stated in Pipfile.lock."""
    for package_version in chain(generated_project.pipfile_lock.packages, generated_project.pipfile_lock.dev_packages):
        if package_version.hashes:
            # Already filled from the last run.
            continue

        if package_version.index:
            scanned_hashes = package_version.index.get_package_hashes(
                package_version.name, package_version.locked_version
            )
        else:
            for source in generated_project.pipfile.meta.sources.values():
                try:
                    scanned_hashes = source.get_package_hashes(package_version.name, package_version.locked_version)
                    break
                except Exception:
                    continue
            else:
                raise ValueError("Unable to find package hashes")

        for entry in scanned_hashes:
            package_version.hashes.append("sha256:" + entry["sha256"])

    return generated_project
