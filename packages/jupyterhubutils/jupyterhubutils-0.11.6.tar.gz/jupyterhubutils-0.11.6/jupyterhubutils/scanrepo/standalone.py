#!/usr/bin/env python3
import argparse
from .scanrepo import ScanRepo


def standalone():
    '''Standalone command for scanning repo.
    '''
    args = parse_args()
    scanner = ScanRepo(host=args.repo,
                       path=args.path,
                       owner=args.owner,
                       name=args.name,
                       dailies=args.dailies,
                       weeklies=args.weeklies,
                       releases=args.releases,
                       experimentals=args.experimentals,
                       recommended=args.recommended,
                       json=args.json,
                       insecure=args.insecure,
                       sort_field=args.sort,
                       cachefile=args.cachefile,
                       debug=args.debug)
    scanner.scan()
    scanner.report()


def parse_args():
    '''Parse command-line arguments.
    '''
    desc = "Get list of Lab Images for display or prepulling"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debugging")
    parser.add_argument("-r", "--repo", "--repository",
                        help="Docker repository host")
    parser.add_argument("-o", "--owner", "--organization", "--org",
                        help="repository owner [lsstsqre]",
                        default="lsstsqre")
    parser.add_argument("-n", "--name",
                        help="repository name [sciplat-lab]",
                        default="sciplat-lab")
    parser.add_argument("-q", "--dailies", "--daily", "--quotidian", type=int,
                        help="# of daily builds to keep [3]",
                        default=3)
    parser.add_argument("-w", "--weeklies", "--weekly", type=int,
                        help="# of weekly builds to keep [2]",
                        default=2)
    parser.add_argument("-e", "--experimentals", "--experimental",
                        "--exp", type=int,
                        help="# of experimental builds to keep [0]",
                        default=0)
    parser.add_argument("-b", "--releases", "--release", type=int,
                        help="# of release builds to keep [1]",
                        default=1)
    parser.add_argument("-c", "--recommended", type=bool,
                        help="select 'recommended' tag [True]",
                        default=True)
    parser.add_argument("-i", "--insecure", "--no-tls", "--no-ssl",
                        help="Do not use TLS to connect [False]",
                        action='store_true',
                        default=False)
    parser.add_argument("-l", "--list", "--list-images", "--image-list",
                        help=("Use supplied comma-separated list in" +
                              " addition to repo scan"))
    parser.add_argument("-p", "--port", help="Repository port [443 for" +
                        " secure, 80 for insecure]",
                        default=None)
    parser.add_argument("-s", "--sort", "--sort-field", "--sort-by",
                        help="Field to sort results by [name]",
                        default="name")
    parser.add_argument("-j", "--json", help="Emit results as JSON, " +
                        " not sourceable shell fragment [False]",
                        action='store_true',
                        default=False)
    parser.add_argument("-f", "--cachefile", help="Cachefile for results " +
                        " [None]", default=None)
    results = parser.parse_args()
    results.path = ("/v2/repositories/" + results.owner + "/" +
                    results.name + "/tags/")
    if results.list:
        results.list = list(set(results.list.split(',')))
    return results


if __name__ == "__main__":
    standalone()
