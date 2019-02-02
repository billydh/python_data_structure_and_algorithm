class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dest_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')

            dest_email = '@'.join([local, domain])

            dest_emails.add(dest_email)

        return len(dest_emails)


# test cases
# solution = Solution()
#
# test = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']
# solution.numUniqueEmails(test)
