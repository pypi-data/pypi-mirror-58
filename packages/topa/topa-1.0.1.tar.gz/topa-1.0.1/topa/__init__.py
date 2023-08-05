import re
from functools import reduce

import click

VERSION = '1.0.1'
GITHUB_URL = 'https://github.com/jwenjian/topa'
PID_LINE_REG_PATTERN = r'[ ]*[\d]+[ ]*[\S\s]+'


class ReportOfPid:
    def __init__(self):
        self.pid = None
        self.max_cpu = None
        self.min_cpu = None
        self.avg_cpu = None
        self.max_mem = None
        self.min_mem = None
        self.avg_mem = None
        self.total_count = None
        pass


class LineObj:
    def __init__(self, parsed_fields):
        self.pid = parsed_fields[0]
        self.user = parsed_fields[1]
        self.pr = parsed_fields[2]
        self.ni = parsed_fields[3]
        self.virt = parsed_fields[4]
        self.res = parsed_fields[5]
        self.shr = parsed_fields[6]
        self.s = parsed_fields[7]
        self.cpu = parsed_fields[8]
        self.mem = parsed_fields[9]
        self.time = parsed_fields[10]
        self.command = parsed_fields[11]


class DefaultHelp(click.Command):
    """
    If no arguments, show help info
    """

    def __init__(self, *args, **kwargs):
        context_settings = kwargs.setdefault('context_settings', {})
        if 'help_option_names' not in context_settings:
            context_settings['help_option_names'] = ['-h', '--help']
        self.help_flag = context_settings['help_option_names'][0]
        super(DefaultHelp, self).__init__(*args, **kwargs)

    def parse_args(self, ctx, args):
        if not args:
            args = [self.help_flag]
        return super(DefaultHelp, self).parse_args(ctx, args)


def print_banner():
    click.echo(r'''```
   _               _ __          
  | |_     ___    | '_ \  __ _   
  |  _|   / _ \   | .__/ / _` |  
  _\__|   \___/   |_|__  \__,_|  
_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  {}, by {}
```'''.format(VERSION, GITHUB_URL))


def get_line_count(filename):
    count = -1
    for count, line in enumerate(open(filename, 'r')):
        count += 1
    return count


def read_all_lines(filename, pid):
    click.echo()
    click.echo('# Reading')
    total_line_count = get_line_count(filename)
    lines = []
    with open(filename) as f:
        line_str = f.readline()
        processed_count = 1
        with click.progressbar(length=total_line_count, label='Reading `{}`'.format(filename)) as bar:
            while line_str is not None and len(line_str) > 0:
                processed_count += 1
                bar.update(1)
                if pid and len(pid) > 0:
                    for p in pid:
                        if line_str.lstrip().startswith(str(p)):
                            lines.append(line_str.lstrip())
                            break
                else:
                    lines.append(line_str.lstrip())
                line_str = f.readline()

    click.echo()
    click.echo('Done!')

    return lines


def line_str_to_info_obj(line: str):
    fields = list(filter(lambda f: len(f) > 0, line.split(' ')))
    return LineObj(fields)


def do_analyze(all_pid_info_lines, pid) -> list:
    report_list = []

    filtered = list(filter(
        lambda i: pid is None or len(pid) == 0 or i.pid in pid,
        # line info to LineObj
        map(
            lambda line: line_str_to_info_obj(line),
            all_pid_info_lines
        )
    ))

    group_result = {}

    for item in filtered:
        _pid = item.pid
        if _pid not in group_result:
            group_result[_pid] = []
        group_result[_pid].append(item)

    for p in group_result:
        if pid and len(pid) > 0 and p not in pid:
            continue
        report_of_pid = ReportOfPid()
        lines_of_pid = group_result[p]
        report_of_pid.pid = p
        report_of_pid.total_count = len(lines_of_pid)

        def sort_by_cpu(l: LineObj):
            return float(l.cpu)

        def sort_by_mem(l: LineObj):
            return float(l.mem)

        lines_of_pid.sort(key=sort_by_cpu, reverse=True)
        max_cpu_obj = lines_of_pid[0]
        min_cpu_obj = lines_of_pid[-1]
        avg_cpu = reduce(lambda i, j: i + j, map(lambda i: float(i.cpu), lines_of_pid.__iter__())) / len(
            lines_of_pid)
        report_of_pid.max_cpu = max_cpu_obj.cpu
        report_of_pid.min_cpu = min_cpu_obj.cpu
        report_of_pid.avg_cpu = avg_cpu
        lines_of_pid.sort(key=sort_by_mem, reverse=True)
        max_mem_obj = lines_of_pid[0]
        min_mem_obj = lines_of_pid[-1]
        avg_mem = reduce(lambda i, j: i + j, map(lambda i: float(i.mem), lines_of_pid.__iter__())) / len(
            lines_of_pid)
        report_of_pid.max_mem = max_mem_obj.mem
        report_of_pid.min_mem = min_mem_obj.mem
        report_of_pid.avg_mem = avg_mem
        report_list.append(report_of_pid)
    return report_list


def show_report(report_list: list) -> None:
    click.echo()
    click.echo('# Reporting ')
    click.echo('Report of `{}` process(es) ready in below'.format(len(report_list)))
    click.echo()
    for report_of_pid in report_list:
        click.echo('## Pid = {}'.format(report_of_pid.pid))
        click.echo('- Total record count = {}'.format(report_of_pid.total_count))
        click.echo('- Max CPU = {}%'.format(report_of_pid.max_cpu))
        click.echo('- Min CPU = {}%'.format(report_of_pid.min_cpu))
        click.echo('- Avg CPU = {:.2f}%'.format(report_of_pid.avg_cpu))
        click.echo('- Max MEM = {}%'.format(report_of_pid.max_mem))
        click.echo('- Min MEM = {}%'.format(report_of_pid.min_mem))
        click.echo('- Avg MEM = {:.2f}%'.format(report_of_pid.avg_mem))
        click.echo()


@click.command(cls=DefaultHelp)
@click.argument('filename', type=click.Path(exists=True))
@click.option('--pid', '-p', nargs=1, multiple=True, required=False, type=str, help='The pid list to be analyzed')
@click.option('--out', '-o', nargs=1, multiple=False, default='STD', show_default=True,
              type=click.Choice(['STD', 'PDF'], case_sensitive=False),
              help='The analyze report file format')
def main(pid, out, filename):
    """
    TOPA - Top Output Python Analyzer

    A python cli application to analyze standard linux top output

    """

    # banner
    print_banner()

    # read top output files
    all_lines = read_all_lines(filename, pid)

    # pid info lines only
    def starts_with_pid(line: str):
        return re.match(PID_LINE_REG_PATTERN, line)

    pid_info_lines = list(filter(starts_with_pid, all_lines))

    # do analyze
    report_list = do_analyze(pid_info_lines, pid)

    # show report
    show_report(report_list)


if __name__ == '__main__':
    main()
