{{#general_title}}
# {{{title}}}

{{/general_title}}

{{#versions}}
{{#solicited_requests}}### {{{solicited_requests}}}{{/solicited_requests}}

{{#sections}}

{{#commits}}

{{#tags}}#{{{tags}}}{{/tags}}

{{#links_or_not}}### **[{{{second_parameter}}}]({{{jira_url}}}/{{{second_parameter}}})**{{/links_or_not}}{{^links_or_not}}{{{second_parameter}}}{{/links_or_not}}

**DATE:** {{{date}}}

**TITLE:** {{{commit_title}}}

{{#body}}{{{body_indented}}}{{/body}}

* * *

{{/commits}}
{{/sections}}

{{/versions}}
