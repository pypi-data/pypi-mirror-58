import os
import re
import time
import javalang
from subprocess import Popen
from robobrowser import RoboBrowser
from prettytable import PrettyTable

from . import cf_login
from .cf_colors import colors
from .codeforces import CodeforcesAPI

dir_path = os.getcwd()


# Hack problems

def hack(contest, hack_test, submission_id):
    browser = cf_login.login()
    browser.open('https://codeforces.com/contest/' +
                 contest + '/challenge/' + str(submission_id))
    hack_form = browser.get_form(class_='challenge-form')
    hack_form['testcaseFromFile'] = hack_test
    browser.submit_form(hack_form)


def tle_hack(contest, heck_generator, submission_id):
    browser = cf_login.login()
    browser.open('https://codeforces.com/contest/' +
                 contest + '/challenge/' + str(submission_id))
    hack_form = browser.get_form(class_='challenge-form')
    hack_form['generatorSourceFile'] = heck_generator
    hack_form['programTypeId'] = '50'
    browser.submit_form(hack_form)


def comp(source):
    info = source.split('.')
    lang = info[-1]
    if lang == 'cpp':
        Popen('g++ %s -DLOCAL -O2 -o %s' %
              (source, info[0]), shell=True).wait()
        Popen(['mv', info[0], 'workspace']).wait()
    elif lang == 'c':
        Popen('gcc %s -DLOCAL -O2 -o %s' %
              (source, info[0]), shell=True).wait()
        Popen(['mv', info[0], 'workspace']).wait()
    elif lang == 'java':
        Popen('javac %s' % (source), shell=True).wait()
        Popen(['mv', info[0], 'workspace']).wait()
    elif lang == 'kt':
        Popen('kotlinc %s -include-runtime -d %s' %
              (source, info[0]+'.jar'), shell=True).wait()
        Popen(['mv', info[0]+'.jar', 'workspace']).wait()
    elif lang == 'py':
        Popen(['cp', source, 'workspace']).wait()


def init_workspace(generator, tle_generator, checker, correct_solution):
    print('%sInitializing workspace...%s' % (colors.OKGREEN, colors.ENDC))
    Popen(['rm', '-rf', 'workspace']).wait()
    Popen(['mkdir', '-p', 'workspace']).wait()
    comp(generator)
    comp(checker)
    comp(correct_solution)
    if tle_generator is not None:
        Popen(['cp', tle_generator, 'workspace']).wait()
        comp(tle_generator)
    print('%sWorkspace is ready!!%s' % (colors.OKGREEN, colors.ENDC))


def begin_hack(contest, problem, generator, tle_generator, checker, correct_solution, test_number):
    hacked_solutions = 0
    tried_solutions = 0

    # Preparing Workspace
    init_workspace(generator, tle_generator, checker, correct_solution)
    Popen(['touch', 'tried_submissions']).wait()
    tried_submissions_list = open('tried_submissions', 'r')
    list_str = tried_submissions_list.read().strip()
    tried_submissions = list()
    if list_str != '':
        tried_submissions = list(map(int, list_str.split(' ')))
    tried_submissions_list = open('tried_submissions', 'a')

    browser = RoboBrowser(parser='lxml')
    browser.open('https://codeforces.com/contest/' +
                 contest + '/status/' + problem.upper())
    max_pages = int(browser.parsed.find_all(class_='page-index')[-1].text)
    print('\n%sHappy Hacking 3:) - max pages : %d%s' %
          (colors.HEADER, max_pages, colors.ENDC))
    for i in range(max_pages, 0, -1):
        try:
            browser = RoboBrowser(parser='lxml')
            browser.open('https://codeforces.com/contest/%s/status/%s/page/%d?order=BY_ARRIVED_DESC'
                         % (contest, problem.upper(), i))
            submissions = browser.parsed.find_all(
                'table', class_='status-frame-datatable')[0].find_all('tr')[1:]
            for submission in submissions:
                submission_id = int(submission.find(
                    'td', class_='id-cell').find('a').text)
                tried_solutions = tried_solutions + 1
                if submission_id in tried_submissions:
                    print('\n%sSubmission %d on page %d/%d already tried!!%s' %
                          (colors.WARNING, submission_id, i, max_pages, colors.ENDC))
                    continue
                tried_submissions_list.write(str(submission_id) + ' ')
                tried_submissions_list.flush()
                language = submission.find_all(
                    'td')[4].text.strip().replace(' ', '')
                browser = RoboBrowser(parser='lxml')
                browser.open(
                    'http://codeforces.com/contest/%s/submission/%d' % (contest, submission_id))
                if len(browser.parsed.find_all('pre', class_='program-source')) > 0:
                    source = browser.parsed.find_all(
                        'pre', class_='program-source')[0].text
                    file_name = create_file(source, language)
                    if file_name == '':
                        continue
                    print('\n%sHacked : %d, %sFailed : %d, %sTotal : %d%s'
                          % (colors.OKGREEN, hacked_solutions, colors.FAIL,
                             tried_solutions-hacked_solutions,
                             colors.OKBLUE, tried_solutions, colors.ENDC))
                    print('%sTrying to hack a %s solution - %d on page %d/%d...%s'
                          % (colors.HEADER, language, submission_id, i, max_pages, colors.ENDC))
                    print('%sNormal hack process%s' %
                          (colors.WARNING, colors.ENDC))
                    hack_process = Popen(
                        [os.path.join(os.path.dirname(__file__), 'hack_prob.sh'),
                         generator, checker, correct_solution, file_name, language.replace(' ', ''), str(test_number)])
                    hack_process.wait(timeout=10)
                    exit_code = hack_process.returncode
                    if exit_code in [0, 127, 255]:
                        print('%sSorry, can\'t hack this solution x /' %
                              (colors.FAIL))
                    else:
                        test_hack_loc = os.path.join(
                            dir_path, 'workspace', 'failed.txt')
                        if os.path.isfile(test_hack_loc):
                            print('%sHope that will win 3:)%s' %
                                  (colors.OKGREEN, colors.ENDC))
                            hacked_solutions = hacked_solutions + 1
                            hack(contest, test_hack_loc, submission_id)
                            continue
                    if tle_generator is not None:
                        print('%sTLE hack process%s' %
                              (colors.WARNING, colors.ENDC))
                        hack_process = Popen(
                            [os.path.join(os.path.dirname(__file__), 'hack_prob.sh'),
                             tle_generator, checker, correct_solution, file_name, language.replace(' ', ''), str(test_number)])
                        hack_process.wait(timeout=10)
                        exit_code = hack_process.returncode
                        if exit_code in [0, 127, 255]:
                            print('%sSorry, can\'t hack this solution x /' %
                                  (colors.FAIL))
                        else:
                            hack_source_loc = os.path.join(
                                dir_path, 'workspace', tle_generator)
                            if os.path.isfile(hack_source_loc):
                                print('%sHope that will win 3:)%s' %
                                      (colors.OKGREEN, colors.ENDC))
                                hacked_solutions = hacked_solutions + 1
                                tle_hack(contest, hack_source_loc,
                                         submission_id)
        except KeyboardInterrupt:
            time.sleep(2)
            break
        except Exception:
            continue
    print('\n%sRESULT => %sHacked : %d, %sFailed : %d, %sTotal : %d'
          % (colors.HEADER, colors.OKGREEN, hacked_solutions, colors.FAIL,
             tried_solutions-hacked_solutions, colors.OKBLUE, tried_solutions))


def create_file(source, language):
    if re.match(r'(.)*\+\+(.)*', language):
        file_name = 'noncorrect.cpp'
    elif re.match(r'(.)*GNU(.)*', language):
        file_name = 'noncorrect.c'
    elif re.match(r'(.)*Kotlin(.)*', language):
        file_name = 'noncorrect.kt'
    elif re.match(r'(.)*Java(.)*', language):
        try:
            tree = javalang.parse.parse(source)
            name = next(klass.name for klass in tree.types
                        if isinstance(klass, javalang.tree.ClassDeclaration)
                        for m in klass.methods
                        if m.name == 'main' and m.modifiers.issuperset({'public', 'static'}))
            file_name = name + '.java'
        except Exception:
            return ''
    elif re.match(r'(.)*Py(.)*', language):
        file_name = 'noncorrect.py'
    else:
        return ''

    for_hack_source = open(os.path.join(dir_path, 'workspace', file_name), 'w')
    for_hack_source.write(source)
    for_hack_source.close()
    return file_name


def print_standings(contest, limit, show_all):
    if contest is None:
        print('Please specify a contest first using: cf hack standings --contest 1010 or cf con --id 1010')
        return
    codeforces = CodeforcesAPI()
    standings = codeforces.contestStandings(
        contest, count=None, showUnofficial=True)
    rows = standings.rows
    print('Contest:\n   Id:   %s\n   Name: %s' %
          (contest, standings.contest.name))
    data = list()
    standings = PrettyTable()
    standings.field_names = ['Rank', 'Name', 'Hacks']
    standings.align['Name'] = 'l'
    standings.align['Hacks'] = 'l'
    for row in rows:
        handle = None
        if row.party.ghost is True:
            handle = row.party.teamName
        else:
            handle = safe_list_get(row.party.members, 0, {
                                   'handle': None}).handle
        entry = {
            'handle': handle,
            'successfulHackCount': row.successfulHackCount,
            'unsuccessfulHackCount': row.unsuccessfulHackCount
        }
        data.append(entry)

    data.sort(key=lambda item: item['unsuccessfulHackCount'])
    data.sort(key=lambda item: item['successfulHackCount'], reverse=True)
    for i, item in enumerate(data):
        if i >= limit and not show_all:
            break
        standings.add_row(
            [i+1, item['handle'], '+{} : -{}'.format(item['successfulHackCount'], item['unsuccessfulHackCount'])])
    print(standings.get_string(sortby='Rank'))


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default
