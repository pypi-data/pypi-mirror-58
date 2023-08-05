import sys, re, colorama, os, time, linecache
colorama.init()


name = "pretty_errors"

FILENAME_COMPACT  = 0
FILENAME_EXTENDED = 1
FILENAME_FULL     = 2

reset_color = '\033[m'



class PrettyErrorsConfig():
    def __init__(self):
        self.line_length            = 0
        self.full_line_newline      = False
        self.filename_display       = FILENAME_COMPACT
        self.display_timestamp      = False
        self.display_link           = False
        self.seperator_character    = '-'
        self.line_number_first      = False
        self.top_first              = False
        self.stack_depth            = 0
        self.exception_above        = False
        self.exception_below        = True
        self.trace_lines_before     = 0
        self.trace_lines_after      = 0
        self.lines_before           = 0
        self.lines_after            = 0
        self.header_color           = '\033[1;30m'
        self.timestamp_color        = '\033[1;30m'
        self.line_color             = '\033[1;38m'
        self.code_color             = '\033[1;30m'
        self.filename_color         = '\033[1;36m'
        self.line_number_color      = '\033[1;32m'
        self.function_color         = '\033[1;34m'
        self.link_color             = '\033[1;30m'
        self.exception_color        = '\033[1;31m'
        self.exception_arg_color    = '\033[1;35m'
        self.prefix                 = None
        self.infix                  = None
        self.postfix                = None
        self.reset_stdout           = False


    def configure(self, **kwargs):
        """Used to configure settings governing how exceptions are displayed."""
        for setting in kwargs:
            if kwargs[setting] is not None: setattr(self, setting, kwargs[setting])


config = PrettyErrorsConfig()


def configure(line_length = None, filename_display = None, full_line_newline = None,
              display_timestamp = None, display_link = None, seperator_character = None,
              header_color = None, line_color = None, code_color = None,
              timestamp_color = None, filename_color = None, line_number_color = None,
              function_color = None, link_color = None,
              exception_color = None, exception_arg_color = None,
              prefix = None, infix = None, postfix = None,
              trace_lines_before = None, trace_lines_after = None,
              lines_before = None, lines_after = None,
              top_first = None, stack_depth = None, line_number_first = None,
              exception_above = None, exception_below = None, reset_stdout = None):
    """Used to configure settings governing how exceptions are displayed."""
    config.configure(
        line_length            = line_length,
        filename_display       = filename_display,
        full_line_newline      = full_line_newline,
        display_timestamp      = display_timestamp,
        display_link           = display_link,
        seperator_character    = seperator_character,
        header_color           = header_color,
        line_color             = line_color,
        code_color             = code_color,
        timestamp_color        = timestamp_color,
        filename_color         = filename_color,
        line_number_color      = line_number_color,
        function_color         = function_color,
        link_color             = link_color,
        exception_color        = exception_color,
        exception_arg_color    = exception_arg_color,
        prefix                 = prefix,
        infix                  = infix,
        postfix                = postfix,
        exception_above        = exception_above,
        exception_below        = exception_below,
        trace_lines_before     = trace_lines_before,
        trace_lines_after      = trace_lines_after,
        lines_before           = lines_before,
        lines_after            = lines_after,
        top_first              = top_first,
        line_number_first      = line_number_first,
        stack_depth            = stack_depth,
        reset_stdout           = reset_stdout
    )



def excepthook(exception_type, exception_value, traceback):
    "Replaces sys.excepthook to output pretty errors."


    def get_terminal_width():
        try:
            return os.get_terminal_size()[0]
        except Exception:
            return 79


    def get_line_length():
        if config.line_length == 0:
            return get_terminal_width()
        else:
            return config.line_length


    def output_text(texts, newline = False):
        if not isinstance(texts, (list, tuple)):
            texts = [texts]
        count = 0
        for text in texts:
            text = str(text)
            sys.stderr.write(text)
            if not text.startswith('\033'):
                count += len(text)
        line_length = get_line_length()
        if newline and (count == 0 or count % line_length != 0 or config.full_line_newline):
            sys.stderr.write('\n')
        sys.stderr.write(reset_color)
        if config.reset_stdout:
            sys.stdout.write(reset_color)


    def write_header():
        line_length = get_line_length()
        if config.display_timestamp:
            timestamp = str(time.perf_counter())
            seperator = (line_length - len(timestamp)) * config.seperator_character + timestamp
        else:
            seperator = line_length * config.seperator_character
        output_text('\n')
        output_text([config.header_color, seperator], newline = True)


    def write_location(path, line, function):
        line_number = str(line) + ' '
        output_text('\n')
        if config.filename_display == FILENAME_FULL:
            filename = ""
            output_text([config.filename_color, path], newline = True)
            output_text([config.line_number_color, line_number, config.function_color, function], newline = True)
        else:
            if config.filename_display == FILENAME_EXTENDED:
                line_length = get_line_length()
                filename = path[-(line_length - len(line_number) - len(function) - 4):]
                if filename != path:
                    filename = '...' + filename
            else:
                filename = os.path.basename(path)
            if config.line_number_first:
                output_text([
                    config.line_number_color, line_number,
                    config.function_color,    function + ' ',
                    config.filename_color,    filename
                ], newline = True)
            else:
                output_text([
                    config.filename_color,    filename + ' ',
                    config.line_number_color, line_number,
                    config.function_color,    function
                ], newline = True)
        if config.display_link:
            output_text([config.link_color, '"%s", line %s' % (path, line)], newline = True)


    def write_code(filepath, line, module_globals, is_final):
        if is_final:
            target_line = config.lines_before
            start = line - config.lines_before
            end   = line + config.lines_after
        else:
            target_line = config.trace_lines_before
            start = line - config.trace_lines_before
            end   = line + config.trace_lines_after

        if start < 1:
            target_line -= (1 - start)
            start = 1

        lines = []
        for i in range(start, end + 1):
            lines.append(linecache.getline(filepath, i, module_globals).rstrip())

        min_lead = 9999
        for line in lines:
            c = 0
            while c < len(line) and line[c] in (' ', '\t'):
                c += 1
            if c < min_lead: min_lead = c
        if min_lead > 0:
            lines = [line[min_lead:] for line in lines]


        for i, line in enumerate(lines):
            if i == target_line:
                output_text([config.line_color, line], newline = True)
            else:
                output_text([config.code_color, line], newline = True)


    def exception_name(exception):
        label = str(exception)
        if label.startswith("<class '"):
            label = label[8:-2]
        return label


    def write_exception(exception_type, exception_value):
        if len(exception_value.args) > 0:
            output_text([
                config.exception_color, exception_name(exception_type), ':\n',
                config.exception_arg_color, '\n'.join((str(x) for x in exception_value.args))
            ], newline = True)
        else:
            output_text([config.exception_color, exception_name(exception_type)], newline = True)


    write_header()

    if config.prefix != None:
        sys.stderr.write(config.prefix)

    if config.exception_above:
        output_text('', newline = True)
        write_exception(exception_type, exception_value)

    tracebacks = []
    while traceback != None:
        tracebacks.append(traceback)
        traceback = traceback.tb_next

    if config.top_first:
        tracebacks.reverse()
        if config.stack_depth > 0:
            tracebacks = tracebacks[:config.stack_depth]
        final = 0
    else:
        if config.stack_depth > 0:
            tracebacks = tracebacks[-config.stack_depth:]
        final = config.stack_depth - 1

    for count, traceback in enumerate(tracebacks):
        if config.infix != None and count != 0:
            sys.stderr.write(config.infix)

        frame = traceback.tb_frame
        code = frame.f_code
        write_location(code.co_filename, traceback.tb_lineno, code.co_name)
        write_code(code.co_filename, traceback.tb_lineno, frame.f_globals, count == final)

    if config.exception_below:
        output_text('', newline = True)
        write_exception(exception_type, exception_value)

    if config.postfix != None:
        sys.stderr.write(config.postfix)


sys.excepthook = excepthook



if __name__ == "__main__":
    configure(line_number_first = False, filename_display=FILENAME_EXTENDED)
    raise KeyError#("foo", 1)
        #test
