import requests

assertion = 'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c2FtbDJwOlJlc3BvbnNlIERlc3RpbmF0aW9uPSJodHRwczovL2xvZ2luLnVzdzIucHVyZS5jbG91ZC9zYW1sIiBJRD0iaWQzMjU3OTQyNjU3NDExMzUxMDQ1MDMwOTUxIiBJc3N1ZUluc3RhbnQ9IjIwMjMtMTItMjFUMjE6MzM6MTQuMDc1WiIgVmVyc2lvbj0iMi4wIiB4bWxuczpzYW1sMnA9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpwcm90b2NvbCIgeG1sbnM6eHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIj48c2FtbDI6SXNzdWVyIEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6ZW50aXR5IiB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI%2BaHR0cDovL3d3dy5va3RhLmNvbS9leGtkb3lvZTN6T3NrUEhoTzVkNzwvc2FtbDI6SXNzdWVyPjxkczpTaWduYXR1cmUgeG1sbnM6ZHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPjxkczpTaWduZWRJbmZvPjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIi8%2BPGRzOlNpZ25hdHVyZU1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZHNpZy1tb3JlI3JzYS1zaGEyNTYiLz48ZHM6UmVmZXJlbmNlIFVSST0iI2lkMzI1Nzk0MjY1NzQxMTM1MTA0NTAzMDk1MSI%2BPGRzOlRyYW5zZm9ybXM%2BPGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNlbnZlbG9wZWQtc2lnbmF0dXJlIi8%2BPGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI%2BPGVjOkluY2x1c2l2ZU5hbWVzcGFjZXMgUHJlZml4TGlzdD0ieHMiIHhtbG5zOmVjPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiLz48L2RzOlRyYW5zZm9ybT48L2RzOlRyYW5zZm9ybXM%2BPGRzOkRpZ2VzdE1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZW5jI3NoYTI1NiIvPjxkczpEaWdlc3RWYWx1ZT5BVm1mYU45QkxpRXBxMzJaZWw4eGxwM0g4SCtIQVRSU3p0V1VObE12ZUpBPTwvZHM6RGlnZXN0VmFsdWU%2BPC9kczpSZWZlcmVuY2U%2BPC9kczpTaWduZWRJbmZvPjxkczpTaWduYXR1cmVWYWx1ZT5jZTVBRTBGc0xKM3V6V2FNL2VkSXRFYm41MjNPdXRzRzFEMmZVMERzQkt0UGpibGk2SHFjSWFrcVh1c05xWE5lVkQ0aGgzczVkSzdjUDB1ZHZGWVF5TUNJZHRPb0ZKcXd3dCswNFN5bmdGekM3OU9IaDlQRStjbStvbDdIZTFWcnQxWDdmVVdWUVFqTmVLaGcrOXZFLy80QnVkSmVNaTArTlR4TXdYSlA4YzdYV2Z1VXQ2QVhBQmRMWmtlZmJvaDRzdFY5Z3J1UnozS1haeFlUdEZUaVJ3Q0VBTVlFZUNzOXhDajI3S1IwdjkyQy9TUDl2djNlTlRIOXE5RHJxbVI0ZHhNN2Q0c1ZYSFhXdzRIdk91WVJTMVRQYkxvVjQ1S3phN0kwdDVsWkFKL1NPY2pyakszSkttZFBNWW45Ylk4a2VJd1JIdGtncU9NamY2Sjc1VHpaZGc9PTwvZHM6U2lnbmF0dXJlVmFsdWU%2BPGRzOktleUluZm8%2BPGRzOlg1MDlEYXRhPjxkczpYNTA5Q2VydGlmaWNhdGU%2BTUlJRHFEQ0NBcENnQXdJQkFnSUdBWXhCS2JyaU1BMEdDU3FHU0liM0RRRUJDd1VBTUlHVU1Rc3dDUVlEVlFRR0V3SlZVekVUTUJFRwpBMVVFQ0F3S1EyRnNhV1p2Y201cFlURVdNQlFHQTFVRUJ3d05VMkZ1SUVaeVlXNWphWE5qYnpFTk1Bc0dBMVVFQ2d3RVQydDBZVEVVCk1CSUdBMVVFQ3d3TFUxTlBVSEp2ZG1sa1pYSXhGVEFUQmdOVkJBTU1ER1JsZGkwMk1UUXhNVGM1TmpFY01Cb0dDU3FHU0liM0RRRUoKQVJZTmFXNW1iMEJ2YTNSaExtTnZiVEFlRncweU16RXlNRFl5TWpBME1ETmFGdzB6TXpFeU1EWXlNakExTUROYU1JR1VNUXN3Q1FZRApWUVFHRXdKVlV6RVRNQkVHQTFVRUNBd0tRMkZzYVdadmNtNXBZVEVXTUJRR0ExVUVCd3dOVTJGdUlFWnlZVzVqYVhOamJ6RU5NQXNHCkExVUVDZ3dFVDJ0MFlURVVNQklHQTFVRUN3d0xVMU5QVUhKdmRtbGtaWEl4RlRBVEJnTlZCQU1NREdSbGRpMDJNVFF4TVRjNU5qRWMKTUJvR0NTcUdTSWIzRFFFSkFSWU5hVzVtYjBCdmEzUmhMbU52YlRDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQwpnZ0VCQUpwMFVrUm9peVBxOENYcFFDcXNlU1dDeDBWUjRKTEQ3azhXV1M4V1c4MkhQTGV2VFVxUEFXQnBCU3lNV1NrVEY5WmpISThxCkhwU2hxanpxck92YXl2YW1jSnRoUGhtbFdNQjVHREt3dVVZRi8wcFd2Q2hZYXJsUklRWjBrZEJVY3I2QWpTVVo0NkJWNHVRUk9VMXQKQm8yU3g5R0R3QlV3L2hONW1xMXNObWd1b0x4cW1ieFRHTjJjb3FSWVd5dW1QcnVGZWhVa2dQaktNSE9sOWwyUkhSR3hEYWNmaGpuTApXcDVoOEhtSEJpRWFOY3dNV1VGUUkzNUsvVmZ2RnY5R1JHT0Q3UnVnaEtrN3U5YkNFalo2U2xrQUptRVZEakdacUxoY1dNZDZRZ0tTCkVlVTVCMmVaYlZVSzZOTWxwamprS0pPNWEydVFYRlhVdytjRE1vc0hVWWtDQXdFQUFUQU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FRRUEKUEhiUzlpSzFVM25mYzQwZGZYQ3ZXa3dsWlE3UGRzWkl3aWdKUS9ObGUxTEhNQXJxT2xDZzJwajkzSndWeXJ3cjMwOVRNN0pTYzRqcwp4b0t2cXVMM3FZMURrMnJnOHJWRXcyUzFNLzJyL3p4ZlZ0U3pRMVRyd2E0dFA2MUYrT0RrYjVYNUpDNHhYRHQ2WjNHUmVVUEQ3SUF5Ck9LNnd0Q2tMMFM1ZEo0dUVZVVJBLzBpRmNMY3kxWlFFSUdpeDByQ3pQWXBsUU5GcS9SMGVKUVczcUJGTWp3UThYNzZTdDlmajYrUSsKS2h2Rnp4M2ZxOUF4MGxLQktiSGh1RFQ2bU5TelYraE9jMmZnOEVNU2lheGsxbkpNc3lHK2lwK29ZNnRrUzVtTWQyZTYzTWdhbFZxUQpBU1dSbmFrQnU0NGpCc1NqQmZxOGxhQkVZRVZQdjJzcEdjWFREUT09PC9kczpYNTA5Q2VydGlmaWNhdGU%2BPC9kczpYNTA5RGF0YT48L2RzOktleUluZm8%2BPC9kczpTaWduYXR1cmU%2BPHNhbWwycDpTdGF0dXMgeG1sbnM6c2FtbDJwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiPjxzYW1sMnA6U3RhdHVzQ29kZSBWYWx1ZT0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOnN0YXR1czpTdWNjZXNzIi8%2BPC9zYW1sMnA6U3RhdHVzPjxzYW1sMjpBc3NlcnRpb24gSUQ9ImlkMzI1Nzk0MjY1OTE1OTQ5Nzc1MzE0OTQ0IiBJc3N1ZUluc3RhbnQ9IjIwMjMtMTItMjFUMjE6MzM6MTQuMDc1WiIgVmVyc2lvbj0iMi4wIiB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgeG1sbnM6eHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIj48c2FtbDI6SXNzdWVyIEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6ZW50aXR5IiB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI%2BaHR0cDovL3d3dy5va3RhLmNvbS9leGtkb3lvZTN6T3NrUEhoTzVkNzwvc2FtbDI6SXNzdWVyPjxkczpTaWduYXR1cmUgeG1sbnM6ZHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPjxkczpTaWduZWRJbmZvPjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIi8%2BPGRzOlNpZ25hdHVyZU1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZHNpZy1tb3JlI3JzYS1zaGEyNTYiLz48ZHM6UmVmZXJlbmNlIFVSST0iI2lkMzI1Nzk0MjY1OTE1OTQ5Nzc1MzE0OTQ0Ij48ZHM6VHJhbnNmb3Jtcz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmUiLz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIj48ZWM6SW5jbHVzaXZlTmFtZXNwYWNlcyBQcmVmaXhMaXN0PSJ4cyIgeG1sbnM6ZWM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyIvPjwvZHM6VHJhbnNmb3JtPjwvZHM6VHJhbnNmb3Jtcz48ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2Ii8%2BPGRzOkRpZ2VzdFZhbHVlPkJjbFh2ZDNDRVo5dEdEcWd0YzFIcnRnckxES1RsdytnZW5iT3ZtdWdGejA9PC9kczpEaWdlc3RWYWx1ZT48L2RzOlJlZmVyZW5jZT48L2RzOlNpZ25lZEluZm8%2BPGRzOlNpZ25hdHVyZVZhbHVlPmVjdEtFVFE1WGREaFlYZnZaQ2tMTkh5TExNb3V4OEFqWFZ1ZUdvUUp0NUZWM1c3SEIvdVNxeWljdGsrWlBkam5CY1VEVDJ6c2hFUVUzRGxOYmRxZW9mbjJ4UjY1aXZUWTMyNk5wbHoyUG4rWXlXMFNua2hDblpLZHA4Rzc2Vy9rQ0FSWXFkK1pUNlF3K2RLZGFqL0tSVFBKa2Y2R0kzM1pFbk1iTjc2aldFWW11a2VXWWtWYVI0TlA0SXRKRDl1Z3dzOVNZQ0Urbm9pUkFjcThsY0JlUTNXVXdoblhnRmdFT3RvdkFBWjJGellZQ3lMSDZqaCtkM3REVk1nMFdaVG5Jc1N1bXVuUmdvQ2hxVStOSGZ4Y29sN1ZNeS80VVA0dkV6cXBuOUFwcGdFSWIvWjNvUUcyMGdVUFpndWE3Wi83RTZrWDRSY2JwRzc4Q0ZwVW1rdFZ3dz09PC9kczpTaWduYXR1cmVWYWx1ZT48ZHM6S2V5SW5mbz48ZHM6WDUwOURhdGE%2BPGRzOlg1MDlDZXJ0aWZpY2F0ZT5NSUlEcURDQ0FwQ2dBd0lCQWdJR0FZeEJLYnJpTUEwR0NTcUdTSWIzRFFFQkN3VUFNSUdVTVFzd0NRWURWUVFHRXdKVlV6RVRNQkVHCkExVUVDQXdLUTJGc2FXWnZjbTVwWVRFV01CUUdBMVVFQnd3TlUyRnVJRVp5WVc1amFYTmpiekVOTUFzR0ExVUVDZ3dFVDJ0MFlURVUKTUJJR0ExVUVDd3dMVTFOUFVISnZkbWxrWlhJeEZUQVRCZ05WQkFNTURHUmxkaTAyTVRReE1UYzVOakVjTUJvR0NTcUdTSWIzRFFFSgpBUllOYVc1bWIwQnZhM1JoTG1OdmJUQWVGdzB5TXpFeU1EWXlNakEwTUROYUZ3MHpNekV5TURZeU1qQTFNRE5hTUlHVU1Rc3dDUVlEClZRUUdFd0pWVXpFVE1CRUdBMVVFQ0F3S1EyRnNhV1p2Y201cFlURVdNQlFHQTFVRUJ3d05VMkZ1SUVaeVlXNWphWE5qYnpFTk1Bc0cKQTFVRUNnd0VUMnQwWVRFVU1CSUdBMVVFQ3d3TFUxTlBVSEp2ZG1sa1pYSXhGVEFUQmdOVkJBTU1ER1JsZGkwMk1UUXhNVGM1TmpFYwpNQm9HQ1NxR1NJYjNEUUVKQVJZTmFXNW1iMEJ2YTNSaExtTnZiVENDQVNJd0RRWUpLb1pJaHZjTkFRRUJCUUFEZ2dFUEFEQ0NBUW9DCmdnRUJBSnAwVWtSb2l5UHE4Q1hwUUNxc2VTV0N4MFZSNEpMRDdrOFdXUzhXVzgySFBMZXZUVXFQQVdCcEJTeU1XU2tURjlaakhJOHEKSHBTaHFqenFyT3ZheXZhbWNKdGhQaG1sV01CNUdES3d1VVlGLzBwV3ZDaFlhcmxSSVFaMGtkQlVjcjZBalNVWjQ2QlY0dVFST1UxdApCbzJTeDlHRHdCVXcvaE41bXExc05tZ3VvTHhxbWJ4VEdOMmNvcVJZV3l1bVBydUZlaFVrZ1BqS01IT2w5bDJSSFJHeERhY2Zoam5MCldwNWg4SG1IQmlFYU5jd01XVUZRSTM1Sy9WZnZGdjlHUkdPRDdSdWdoS2s3dTliQ0VqWjZTbGtBSm1FVkRqR1pxTGhjV01kNlFnS1MKRWVVNUIyZVpiVlVLNk5NbHBqamtLSk81YTJ1UVhGWFV3K2NETW9zSFVZa0NBd0VBQVRBTkJna3Foa2lHOXcwQkFRc0ZBQU9DQVFFQQpQSGJTOWlLMVUzbmZjNDBkZlhDdldrd2xaUTdQZHNaSXdpZ0pRL05sZTFMSE1BcnFPbENnMnBqOTNKd1Z5cndyMzA5VE03SlNjNGpzCnhvS3ZxdUwzcVkxRGsycmc4clZFdzJTMU0vMnIvenhmVnRTelExVHJ3YTR0UDYxRitPRGtiNVg1SkM0eFhEdDZaM0dSZVVQRDdJQXkKT0s2d3RDa0wwUzVkSjR1RVlVUkEvMGlGY0xjeTFaUUVJR2l4MHJDelBZcGxRTkZxL1IwZUpRVzNxQkZNandROFg3NlN0OWZqNitRKwpLaHZGengzZnE5QXgwbEtCS2JIaHVEVDZtTlN6VitoT2MyZmc4RU1TaWF4azFuSk1zeUcraXArb1k2dGtTNW1NZDJlNjNNZ2FsVnFRCkFTV1JuYWtCdTQ0akJzU2pCZnE4bGFCRVlFVlB2MnNwR2NYVERRPT08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48c2FtbDI6U3ViamVjdCB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI%2BPHNhbWwyOk5hbWVJRCBGb3JtYXQ9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMTpuYW1laWQtZm9ybWF0OnVuc3BlY2lmaWVkIj5vcmxhbmRvLm1vbnRhbHZvQGdlbmVzeXMuY29tPC9zYW1sMjpOYW1lSUQ%2BPHNhbWwyOlN1YmplY3RDb25maXJtYXRpb24gTWV0aG9kPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y206YmVhcmVyIj48c2FtbDI6U3ViamVjdENvbmZpcm1hdGlvbkRhdGEgTm90T25PckFmdGVyPSIyMDIzLTEyLTIxVDIxOjM4OjE0LjA3NloiIFJlY2lwaWVudD0iaHR0cHM6Ly9sb2dpbi51c3cyLnB1cmUuY2xvdWQvc2FtbCIvPjwvc2FtbDI6U3ViamVjdENvbmZpcm1hdGlvbj48L3NhbWwyOlN1YmplY3Q%2BPHNhbWwyOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDIzLTEyLTIxVDIxOjI4OjE0LjA3NloiIE5vdE9uT3JBZnRlcj0iMjAyMy0xMi0yMVQyMTozODoxNC4wNzZaIiB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI%2BPHNhbWwyOkF1ZGllbmNlUmVzdHJpY3Rpb24%2BPHNhbWwyOkF1ZGllbmNlPmh0dHBzOi8vbG9naW4udXN3Mi5wdXJlLmNsb3VkL3NhbWw8L3NhbWwyOkF1ZGllbmNlPjwvc2FtbDI6QXVkaWVuY2VSZXN0cmljdGlvbj48L3NhbWwyOkNvbmRpdGlvbnM%2BPHNhbWwyOkF1dGhuU3RhdGVtZW50IEF1dGhuSW5zdGFudD0iMjAyMy0xMi0yMVQyMTozMzoxNC4wNzVaIiBTZXNzaW9uSW5kZXg9ImlkMTcwMzE5NDM5MzcxMS4xNDc1ODg4MzU1IiB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI%2BPHNhbWwyOkF1dGhuQ29udGV4dD48c2FtbDI6QXV0aG5Db250ZXh0Q2xhc3NSZWY%2BdXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFjOmNsYXNzZXM6UGFzc3dvcmRQcm90ZWN0ZWRUcmFuc3BvcnQ8L3NhbWwyOkF1dGhuQ29udGV4dENsYXNzUmVmPjwvc2FtbDI6QXV0aG5Db250ZXh0Pjwvc2FtbDI6QXV0aG5TdGF0ZW1lbnQ%2BPHNhbWwyOkF0dHJpYnV0ZVN0YXRlbWVudCB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI%2BPHNhbWwyOkF0dHJpYnV0ZSBOYW1lPSJPcmdhbml6YXRpb25OYW1lIiBOYW1lRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXR0cm5hbWUtZm9ybWF0OnVuc3BlY2lmaWVkIj48c2FtbDI6QXR0cmlidXRlVmFsdWUgeG1sbnM6eHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4c2k6dHlwZT0ieHM6c3RyaW5nIj5vbW9udGFsdm9kZXY8L3NhbWwyOkF0dHJpYnV0ZVZhbHVlPjwvc2FtbDI6QXR0cmlidXRlPjwvc2FtbDI6QXR0cmlidXRlU3RhdGVtZW50Pjwvc2FtbDI6QXNzZXJ0aW9uPjwvc2FtbDJwOlJlc3BvbnNlPg%3D%3D'

url = "https://login.usw2.pure.cloud/oauth/token?grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion="+assertion+"&orgName=omontalvoDev"


#manually created saml assertion
payload = {}
files={}
headers = {
  'Authorization': 'Basic YThiMjBlY2YtYzJmOS00ODU4LTkyMTAtNTI2OGE2ZGRjODQ2OnR2WER1b0dQSE0zclppVmtzZDVWcFVOT05zYmtjVEdwNjJwLXlDczdKRlU=',
  'Cookie': 'ININ-Auth-Session=mlH1mS6Qg54TOkWVNsojHVwN_N19P79kp8x8BkCaef4='
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
